from src.views.windows.pages.ui_MedicinePage import *
from src.models.database import Database
from src.models.medicine import Medicine
from PySide6.QtWidgets import QButtonGroup
from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMessageBox
import math
from datetime import date
class MedicinePage(QWidget):
    selectionButtons = QButtonGroup()
    timer = QTimer()
    db = Database()
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.ui = Ui_MedicinePage()
        self.mainWindow = mainWindow
        self.ui.setupUi(self)
        self.ui.pushButton.clicked.connect(self._Search_For)
        self.ui.reset_pushButton.clicked.connect(self._Reset_Button)
        self._view_medicine(self.db.cursor.execute("SELECT expiration_date,name FROM Medicine"))

    def _Search_For(self):
        self._view_medicine(self.db.cursor.execute("SELECT expiration_date,name FROM Medicine WHERE name=?",(self.ui.search_lineEdit.text(),)))
    def _Reset_Button(self):
        self._view_medicine(self.db.cursor.execute("SELECT expiration_date,name FROM Medicine"))
    def _view_medicine(self,result):
        self.__Clear__Buttons()
        medicineExDate= list()
        medicineNames = list()
        for row in result.fetchall():
            medicineExDate.append(row[0])
            medicineNames.append(row[1])
        #medicineNames = [name[1] for name in result.fetchall()]
        rows = math.ceil(len(medicineNames)/3)
        count = 1
        for row in range(rows):  
            for column in range(3):
                if count > len(medicineNames):
                    break
                self.ui.buttons_gridLayout.addWidget(self._create_button(medicineNames[count-1],medicineExDate[count-1]),row,column)
                count +=1
    
    def _create_button(self,name,dateEx):
        button = QPushButton(name)
        if(Medicine.is_expired(dateEx)):
           button.setEnabled(False)
           button.setStyleSheet("""
                    QPushButton {
                        background-color: red; 
                        color: white;
                    }
                    QPushButton:hover {
                        background-color: red;  
                    }
                """)

        else:
            button.clicked.connect(lambda: self._On_click(button.text()))
        self.selectionButtons.addButton(button)
        return button
    def _On_click(self,medicineName):
        self.db.cursor.execute("SELECT * from Medicine WHERE name=?",(medicineName,))
        result= self.db.cursor.fetchone()
        medicine = Medicine(
            result[1],
            result[2],
            result[3],
            result[4],
            result[5],
            result[6],
            result[7]
        )
        if(medicine.drawerNumber == 1 and self.mainWindow.current_staff[2] == 'Nurse'):
            QMessageBox.warning(self,"Error","Access denied")
        else:
            Medicine.dispenseMedicine(medicine,int(self.ui.quantity_doubleSpinBox.text()),self.mainWindow.current_staff[0])
            medicine.openDrawer(self.mainWindow.port) 
            self.__Disable_Selection_Buttons()
            self.timer.timeout.connect(lambda: self.__Enable_Selection_Buttons(medicine))
            self.timer.start(10000)

    def __Disable_Selection_Buttons(self):
        for button in self.selectionButtons.buttons():
           button.setEnabled(False)
    def __Enable_Selection_Buttons(self,medicine):
        quantity = int(self.ui.quantity_doubleSpinBox.text())
        medicineID = medicine.get_medicineID()
        medicine.closeDrawer(self.mainWindow.port,self.mainWindow.current_staff[1],medicineID,quantity,self.mainWindow.current_patient.name)
        for button in self.selectionButtons.buttons():
            button.setEnabled(True)
        self.timer.stop()
        self.timer = QTimer()
    def __Clear__Buttons(self):
        widget = self.ui.scrollArea.widget()
        if widget:
            for button in widget.children():
                if isinstance(button,QPushButton):
                    button.deleteLater()
            widget.setLayout(None)