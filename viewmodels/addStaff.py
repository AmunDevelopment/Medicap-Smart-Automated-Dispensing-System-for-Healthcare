from src.views.windows.pages.ui_AddStaffPage import *
from src.ai.camera import Camera
from src.models.staff import Staff
from PySide6.QtWidgets import QMessageBox
from datetime import datetime

class AddStaffPage(QWidget):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    def __init__(self,parent = None):
        QWidget.__init__(self)
        self.ui = Ui_addStaffPage()
        self.ui.setupUi(self)
        self.ui.Add_PushButton.clicked.connect(self._Add_Staff)

        self.cameraInit = Camera(self.ui.camera_label)
        
        self.cameraInit.imgName = f'captured_{self.timestamp}'
        self.ui.capture_pushButton.clicked.connect(self.cameraInit.setup_camera)
    
    def _Add_Staff(self):
        if self.__Validate_Input() and self.__Validate_faceID():
            name = self.ui.name_lineEdit.text()
            birthDate = self.ui.date_dateEdit.text()
            contact = self.ui.contact_lineEdit.text()
            gender = self.ui.gender_ComboBox.currentText()
            role = self.ui.role_ComboBox.currentText()
            faceID = self.cameraInit.faceID     
            staff = Staff(
                name,
                birthDate,
                gender,
                contact,
                faceID,
                role
            )
            staff.uploadDatabase()
            self.__Clear_All()
            QMessageBox.warning(self,"Done","Staff has been added.")
    
    def __Validate_Input(self):
        if (not self.ui.name_lineEdit.text().strip() or not self.ui.contact_lineEdit.text().strip()):
            QMessageBox.warning(self,"Error","Input cannot be Empty")
            return False
        return True
    def __Validate_faceID(self):
        if self.cameraInit.faceID == None:
            QMessageBox.warning(self,"Error","Please take a picture")
            return False
        return True
        
    def __Clear_All(self):
        self.ui.name_lineEdit.clear()
        self.ui.contact_lineEdit.clear()