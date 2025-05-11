from src.views.windows.pages.ui_mainWindow import *
from src.viewmodels.authenticationPage import *
from src.viewmodels.adminPage import *
from src.viewmodels.medicinePage import *
from src.viewmodels.logPage import *
from src.viewmodels.viewPatientPage import *
from src.models.database import Database
from src.models.patient import Patient
import serial,time
import serial.tools.list_ports

class MainWindow(QMainWindow):
    current_staff = None
    current_patient = None
    port = None
    def __init__(self, parent=None):
        QMainWindow.__init__(self)
        self.__Initialize_UART()
        self.__Get_Current_Patient()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.goto_authenticationPage()
        self.ui.admin_PushButton.clicked.connect(lambda: self.goto_page(adminPage(self)))
        self.ui.medicine_pushButton.clicked.connect(lambda: self.goto_page(MedicinePage(self)))
        self.ui.log_pushButton.clicked.connect(lambda: self.goto_page(LogPage()))
        self.ui.patient_pushButton.clicked.connect(lambda: self.goto_page(ViewPatientPage(self)))

    def _Enable_Dashboard_Buttons(self):
       for button in self.ui.dashBoard_Buttons.buttons():
           button.setEnabled(True)
    def _Disable_Dashboard_Buttons(self):
       for button in self.ui.dashBoard_Buttons.buttons():
           button.setEnabled(False)

    def goto_authenticationPage(self):
        self._Disable_Dashboard_Buttons()
        page = authenticationPage(self)
        page.timer.timeout.connect(lambda: page.check_action(self._Enable_Dashboard_Buttons))
        page.timer.start(1000)
        self.ui.main_stackwidget.removeWidget(self.ui.main_stackwidget.currentWidget())
        self.ui.main_stackwidget.addWidget(page)
        self.ui.main_stackwidget.setCurrentWidget(page)

    def goto_page(self,page):
        self.ui.main_stackwidget.removeWidget(self.ui.main_stackwidget.currentWidget())
        self.ui.main_stackwidget.addWidget(page)
        self.ui.main_stackwidget.setCurrentWidget(page)
    
    def __Initialize_UART(self):
        # List available ports
        available_ports = [port.device for port in serial.tools.list_ports.comports()]
        self.port = serial.Serial(port=available_ports[0], baudrate=19200)
        time.sleep(1)
    
    def __Get_Current_Patient(self):
        db = Database()
        result = db.cursor.execute("SELECT * FROM Patient")
        result = result.fetchone()
        patient = Patient(
            result[1],
            result[5],
            result[2],
            result[3],
            result[4]
        )
        self.current_patient = patient