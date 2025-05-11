# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainWindowTYbEPg.ui'
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QGridLayout, QHBoxLayout,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QSpacerItem, QStackedWidget, QVBoxLayout, QWidget)
import src.views.assets.resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(800, 480)
        MainWindow.setMinimumSize(QSize(800, 480))
        MainWindow.setStyleSheet(u"background-color: rgb(245, 250, 254);\n"
"font: 9pt \"Segoe UI\";\n"
"color: rgb(0, 0, 0);")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.horizontalLayout = QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setSpacing(0)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.dashBoard_widget = QWidget(self.centralwidget)
        self.dashBoard_widget.setObjectName(u"dashBoard_widget")
        self.dashBoard_widget.setMinimumSize(QSize(200, 0))
        self.dashBoard_widget.setMaximumSize(QSize(200, 16777215))
        self.dashBoard_widget.setStyleSheet(u"QWidget{\n"
"	\n"
"background-color: rgb(0, 173, 181);\n"
"}\n"
"QPushButton{\n"
"	text-align:left;\n"
"	height: 40px;\n"
"	border: none;\n"
"	font: 700 14pt\"Sans Serif Collection\";\n"
"	\n"
"	color: rgb(255, 255, 255);\n"
"	padding-left: 10px;\n"
"	border-top-left-radius:10px;\n"
"	border-bottom-left-radius:10px;\n"
"}\n"
"QPushButton:checked{\n"
"	background-color: rgb(255, 255, 255);\n"
"	color:#1F95EF;\n"
"}")
        self.verticalLayout_3 = QVBoxLayout(self.dashBoard_widget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, 0, -1)
        self.verticalSpacer_4 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_4)

        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        self.verticalLayout_3.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.admin_PushButton = QPushButton(self.dashBoard_widget)
        self.dashBoard_Buttons = QButtonGroup(MainWindow)
        self.dashBoard_Buttons.setObjectName(u"dashBoard_Buttons")
        self.dashBoard_Buttons.addButton(self.admin_PushButton)
        self.admin_PushButton.setObjectName(u"admin_PushButton")
        self.admin_PushButton.setEnabled(True)
        icon = QIcon()
        icon.addFile(u":/icons/icons/admin.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.admin_PushButton.setIcon(icon)
        self.admin_PushButton.setIconSize(QSize(30, 30))
        self.admin_PushButton.setCheckable(True)
        self.admin_PushButton.setAutoExclusive(True)
        self.admin_PushButton.setFlat(False)

        self.verticalLayout.addWidget(self.admin_PushButton)

        self.medicine_pushButton = QPushButton(self.dashBoard_widget)
        self.dashBoard_Buttons.addButton(self.medicine_pushButton)
        self.medicine_pushButton.setObjectName(u"medicine_pushButton")
        self.medicine_pushButton.setEnabled(True)
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/medicine.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.medicine_pushButton.setIcon(icon1)
        self.medicine_pushButton.setIconSize(QSize(30, 30))
        self.medicine_pushButton.setCheckable(True)
        self.medicine_pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.medicine_pushButton)

        self.patient_pushButton = QPushButton(self.dashBoard_widget)
        self.dashBoard_Buttons.addButton(self.patient_pushButton)
        self.patient_pushButton.setObjectName(u"patient_pushButton")
        self.patient_pushButton.setEnabled(False)
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/patient.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.patient_pushButton.setIcon(icon2)
        self.patient_pushButton.setIconSize(QSize(30, 30))
        self.patient_pushButton.setCheckable(True)
        self.patient_pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.patient_pushButton)

        self.log_pushButton = QPushButton(self.dashBoard_widget)
        self.dashBoard_Buttons.addButton(self.log_pushButton)
        self.log_pushButton.setObjectName(u"log_pushButton")
        self.log_pushButton.setEnabled(False)
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/log.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.log_pushButton.setIcon(icon3)
        self.log_pushButton.setIconSize(QSize(30, 30))
        self.log_pushButton.setCheckable(True)
        self.log_pushButton.setAutoExclusive(True)

        self.verticalLayout.addWidget(self.log_pushButton)


        self.verticalLayout_3.addLayout(self.verticalLayout)

        self.verticalSpacer_2 = QSpacerItem(20, 100, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addWidget(self.dashBoard_widget)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.title_Label = QLabel(self.centralwidget)
        self.title_Label.setObjectName(u"title_Label")
        self.title_Label.setMinimumSize(QSize(0, 50))
        self.title_Label.setMaximumSize(QSize(16777215, 50))
        self.title_Label.setStyleSheet(u"font:700 16pt \"Microsoft YaHei UI\";\n"
"color: rgb(0, 0, 0);")
        self.title_Label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_4.addWidget(self.title_Label)

        self.main_stackwidget = QStackedWidget(self.centralwidget)
        self.main_stackwidget.setObjectName(u"main_stackwidget")
        self.main_stackwidget.setStyleSheet(u"Qlabel{\n"
"	font: 700 16pt \"Segoe UI\";\n"
"	color: rgb(0, 85, 255);\n"
"}")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.gridLayout_2 = QGridLayout(self.page)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_stackwidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.main_stackwidget.addWidget(self.page_2)

        self.verticalLayout_4.addWidget(self.main_stackwidget)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.admin_PushButton.setDefault(False)
        self.main_stackwidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.admin_PushButton.setText(QCoreApplication.translate("MainWindow", u"Admin", None))
        self.medicine_pushButton.setText(QCoreApplication.translate("MainWindow", u"Medicine", None))
        self.patient_pushButton.setText(QCoreApplication.translate("MainWindow", u"Patient", None))
        self.log_pushButton.setText(QCoreApplication.translate("MainWindow", u"Logs", None))
        self.title_Label.setText(QCoreApplication.translate("MainWindow", u"Welcome to ADC", None))
    # retranslateUi

