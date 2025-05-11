# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'dataViewPageQhazrQ.ui'
##
## Created by: Qt User Interface Compiler version 6.9.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QHeaderView,
    QLineEdit, QPushButton, QSizePolicy, QSpacerItem,
    QTableView, QVBoxLayout, QWidget)

class Ui_dataViewPage(object):
    def setupUi(self, dataViewPage):
        if not dataViewPage.objectName():
            dataViewPage.setObjectName(u"dataViewPage")
        dataViewPage.resize(951, 880)
        self.gridLayout = QGridLayout(dataViewPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setHorizontalSpacing(0)
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.searchBar_lineEdit = QLineEdit(dataViewPage)
        self.searchBar_lineEdit.setObjectName(u"searchBar_lineEdit")
        self.searchBar_lineEdit.setMinimumSize(QSize(381, 22))
        self.searchBar_lineEdit.setMaximumSize(QSize(381, 22))
        self.searchBar_lineEdit.setStyleSheet(u"")

        self.verticalLayout.addWidget(self.searchBar_lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)

        self.inventoryData_pushButton = QPushButton(dataViewPage)
        self.inventoryData_pushButton.setObjectName(u"inventoryData_pushButton")
        self.inventoryData_pushButton.setMinimumSize(QSize(75, 24))
        self.inventoryData_pushButton.setMaximumSize(QSize(75, 24))
        self.inventoryData_pushButton.setStyleSheet(u"background-color: rgb(0, 173, 181);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.inventoryData_pushButton)

        self.staffData_pushButton = QPushButton(dataViewPage)
        self.staffData_pushButton.setObjectName(u"staffData_pushButton")
        self.staffData_pushButton.setMinimumSize(QSize(75, 24))
        self.staffData_pushButton.setMaximumSize(QSize(75, 24))
        self.staffData_pushButton.setStyleSheet(u"background-color: rgb(0, 173, 181);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.staffData_pushButton)

        self.patientData_pushButton = QPushButton(dataViewPage)
        self.patientData_pushButton.setObjectName(u"patientData_pushButton")
        self.patientData_pushButton.setMinimumSize(QSize(75, 24))
        self.patientData_pushButton.setMaximumSize(QSize(75, 24))
        self.patientData_pushButton.setStyleSheet(u"background-color: rgb(0, 173, 181);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.patientData_pushButton)

        self.medicineData_pushButton = QPushButton(dataViewPage)
        self.medicineData_pushButton.setObjectName(u"medicineData_pushButton")
        self.medicineData_pushButton.setMinimumSize(QSize(75, 24))
        self.medicineData_pushButton.setMaximumSize(QSize(75, 24))
        self.medicineData_pushButton.setStyleSheet(u"background-color: rgb(0, 173, 181);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.medicineData_pushButton)

        self.logData_pushButton = QPushButton(dataViewPage)
        self.logData_pushButton.setObjectName(u"logData_pushButton")
        self.logData_pushButton.setMinimumSize(QSize(75, 24))
        self.logData_pushButton.setMaximumSize(QSize(75, 24))
        self.logData_pushButton.setStyleSheet(u"background-color: rgb(0, 173, 181);\n"
"font: 700 9pt \"Segoe UI\";")

        self.horizontalLayout.addWidget(self.logData_pushButton)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.gridLayout.addLayout(self.verticalLayout, 0, 0, 1, 1)

        self.dataView_tableView = QTableView(dataViewPage)
        self.dataView_tableView.setObjectName(u"dataView_tableView")
        self.dataView_tableView.setStyleSheet(u"")

        self.gridLayout.addWidget(self.dataView_tableView, 1, 0, 1, 1)


        self.retranslateUi(dataViewPage)

        QMetaObject.connectSlotsByName(dataViewPage)
    # setupUi

    def retranslateUi(self, dataViewPage):
        dataViewPage.setWindowTitle(QCoreApplication.translate("dataViewPage", u"Form", None))
        self.searchBar_lineEdit.setInputMask("")
        self.searchBar_lineEdit.setText("")
        self.inventoryData_pushButton.setText(QCoreApplication.translate("dataViewPage", u"Inventory", None))
        self.staffData_pushButton.setText(QCoreApplication.translate("dataViewPage", u"Staff", None))
        self.patientData_pushButton.setText(QCoreApplication.translate("dataViewPage", u"Patient", None))
        self.medicineData_pushButton.setText(QCoreApplication.translate("dataViewPage", u"Medicine", None))
        self.logData_pushButton.setText(QCoreApplication.translate("dataViewPage", u"Logs", None))
    # retranslateUi

