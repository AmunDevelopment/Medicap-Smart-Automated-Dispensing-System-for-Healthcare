from src.views.windows.pages.ui_LogPage import *
from src.models.database import Database
from PySide6.QtWidgets import QTableWidgetItem
class LogPage(QWidget):
    def __init__(self,parent=None):
        QWidget.__init__(self)
        self.ui = Ui_LogPage()
        self.ui.setupUi(self)

        #Initilizatng  table
        self.__Initilize__Table()
    def __Initilize__Table(self):
        db = Database()
        result = db.cursor.execute("SELECT * FROM Log")
        self.ui.logs_tableWidget.setRowCount(1)
        for row_number,row_data in enumerate(result):
            self.ui.logs_tableWidget.insertRow(row_number)
            for column_number,columm_data in enumerate(row_data):
                self.ui.logs_tableWidget.setItem(row_number,column_number,QTableWidgetItem(str(columm_data)))
