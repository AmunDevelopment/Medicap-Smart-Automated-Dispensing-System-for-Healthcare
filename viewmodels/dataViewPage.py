from src.views.windows.pages.ui_dataViewPage import *
from src.models.database import Database
from PySide6.QtGui import QStandardItemModel , QStandardItem
from PySide6.QtCore import QSortFilterProxyModel,Qt
class DataViewPage(QWidget):
    def __init__(self,parent = None):
        QWidget.__init__(self)
        self.ui = Ui_dataViewPage()
        self.ui.setupUi(self)
        
        # Initiliazing models
        self.tableModel = QStandardItemModel()
        self.search_model = QSortFilterProxyModel()
        self.search_model.setSourceModel(self.tableModel)
        self.search_model.setFilterCaseSensitivity(Qt.CaseInsensitive)
        self.search_model.setFilterKeyColumn(-1) # Search in all columns
        self.ui.dataView_tableView.setModel(self.search_model)
        # View Inventory data by default
        self._viewData("SELECT * FROM Inventory")
        # On button clicked
        self.ui.staffData_pushButton.clicked.connect(lambda: self._viewData("SELECT * FROM Staff"))
        self.ui.inventoryData_pushButton.clicked.connect(lambda: self._viewData("SELECT * FROM Inventory"))
        self.ui.patientData_pushButton.clicked.connect(lambda: self._viewData("SELECT * FROM Patient"))
        self.ui.medicineData_pushButton.clicked.connect(lambda: self._viewData("SELECT * FROM Medicine"))
        self.ui.logData_pushButton.clicked.connect(lambda: self._viewData("SELECT * FROM Log"))
        # Search bar
        self.ui.searchBar_lineEdit.textChanged.connect(self._filter_table)
    
    def _viewData(self,query):
        self.tableModel.clear()
        db = Database()
        result = db.cursor.execute(query)
        column_names = [header[0] for header in db.cursor.description]
        self.tableModel.setHorizontalHeaderLabels(column_names)
        for row in result.fetchall():
            items = [QStandardItem(str(item)) for item in row]
            self.tableModel.appendRow(items)
        self.ui.dataView_tableView.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
    def _filter_table(self):
        self.search_model.setFilterFixedString(self.ui.searchBar_lineEdit.text())
