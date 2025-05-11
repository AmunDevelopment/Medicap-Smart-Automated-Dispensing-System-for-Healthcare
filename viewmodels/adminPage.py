from src.views.windows.pages.ui_adminPage import *
from src.viewmodels.dataViewPage import*
from src.viewmodels.addStaff import *
from src.viewmodels.createPatientPage import *
class adminPage(QWidget):
    def __init__(self,mainWindow):
        QWidget.__init__(self)
        self.mainWindow = mainWindow
        self.ui = Ui_adminPage()
        self.ui.setupUi(self)
        self.ui.addStaff_toolButton.clicked.connect(lambda: self.mainWindow.goto_page(AddStaffPage()))
        self.ui.viewData_toolButton.clicked.connect(lambda: self.mainWindow.goto_page(DataViewPage()))
        self.ui.logout_toolButton.clicked.connect(self.mainWindow.goto_authenticationPage)
        self.ui.camera_toolButton.clicked.connect(lambda: self.mainWindow.goto_page(CreatePatientPage(self.mainWindow)))