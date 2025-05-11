from src.views.windows.pages.ui_ViewPatientPage import *

class ViewPatientPage(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.ui = Ui_ViewPatientPage()
        self.ui.setupUi(self)
        self.mainWindow = mainWindow

        if(self.mainWindow.current_patient !=None):
            self.ui.name_lineEdit.setText(self.mainWindow.current_patient.name)
            self.ui.contact_lineEdit.setText(self.mainWindow.current_patient.contact) 
            self.ui.date_lineEdit.setText(self.mainWindow.current_patient.birthDate)
            self.ui.gender_lineEdit.setText(self.mainWindow.current_patient.gender)
            self.ui.textEdit.setText(self.mainWindow.current_patient.medicalHistory)
    

