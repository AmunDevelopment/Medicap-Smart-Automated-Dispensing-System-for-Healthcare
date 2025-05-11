from src.views.windows.pages.ui_CreatePatientPage import *
from src.models.patient import Patient
from src.models.database import Database

class CreatePatientPage(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.ui = Ui_CreatePatientPage()
        self.ui.setupUi(self)
        self.mainWindow = mainWindow
        self.ui.add_pushButton.clicked.connect(self.__Add__Patient)
    
    def __Add__Patient(self):
        db = Database()
        db.cursor.execute("DELETE FROM patient")
        db.connect.commit()
        patient = Patient(
            self.ui.name_lineEdit.text(),
            self.ui.date_dateEdit.text(),
            self.ui.gender_ComboBox.currentText(),
            self.ui.contact_lineEdit.text(),
            self.ui.medicalHistory_plainTextEdit.toPlainText()
        )
        patient.uploadDatabase()
        self.__Clear_editTexts()
        self.mainWindow.current_patient = patient
    def __Clear_editTexts(self):
            self.ui.name_lineEdit.clear()
            self.ui.date_dateEdit.clear()
            self.ui.contact_lineEdit.text()
            self.ui.medicalHistory_plainTextEdit.clear()