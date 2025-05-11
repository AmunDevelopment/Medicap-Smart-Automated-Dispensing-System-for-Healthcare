

# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'adminPageLYhxxc.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QSizePolicy, QSpacerItem,
    QToolButton, QWidget)
import src.views.assets.resources_rc

class Ui_adminPage(object):
    def setupUi(self, adminPage):
        if not adminPage.objectName():
            adminPage.setObjectName(u"adminPage")
        adminPage.resize(951, 880)
        adminPage.setStyleSheet(u"QToolButton{\n"
"	\n"
"	background-color: rgb(229, 76, 115);\n"
"	border: 2px solid #555;\n"
"	border-radius: 20px;\n"
"	\n"
"	background-color: rgb(57, 62, 70);\n"
"	border-style: outset;\n"
"	font: 700 18pt \"Segoe UI\";\n"
"}\n"
"QToolButton:hover{\n"
"	\n"
"	background-color: rgb(42, 46, 52);\n"
"	color: rgb(197, 197, 197);\n"
"}")
        self.gridLayout_2 = QGridLayout(adminPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalSpacer = QSpacerItem(17, 291, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer, 2, 1, 1, 1)

        self.horizontalSpacer_2 = QSpacerItem(298, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_2, 1, 0, 1, 1)

        self.horizontalSpacer = QSpacerItem(298, 14, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.gridLayout = QGridLayout()
        self.gridLayout.setSpacing(15)
        self.gridLayout.setObjectName(u"gridLayout")
        self.logout_toolButton = QToolButton(adminPage)
        self.logout_toolButton.setObjectName(u"logout_toolButton")
        self.logout_toolButton.setMinimumSize(QSize(151, 121))
        self.logout_toolButton.setMaximumSize(QSize(151, 121))
        self.logout_toolButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon = QIcon()
        icon.addFile(u":/icons/icons/logout.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.logout_toolButton.setIcon(icon)
        self.logout_toolButton.setIconSize(QSize(80, 80))
        self.logout_toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.logout_toolButton, 1, 1, 1, 1)

        self.viewData_toolButton = QToolButton(adminPage)
        self.viewData_toolButton.setObjectName(u"viewData_toolButton")
        self.viewData_toolButton.setMinimumSize(QSize(151, 121))
        self.viewData_toolButton.setMaximumSize(QSize(121, 16777215))
        self.viewData_toolButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon1 = QIcon()
        icon1.addFile(u":/icons/icons/data.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.viewData_toolButton.setIcon(icon1)
        self.viewData_toolButton.setIconSize(QSize(80, 80))
        self.viewData_toolButton.setAutoExclusive(True)
        self.viewData_toolButton.setPopupMode(QToolButton.ToolButtonPopupMode.InstantPopup)
        self.viewData_toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.viewData_toolButton, 0, 1, 1, 1)

        self.addStaff_toolButton = QToolButton(adminPage)
        self.addStaff_toolButton.setObjectName(u"addStaff_toolButton")
        self.addStaff_toolButton.setMinimumSize(QSize(151, 121))
        self.addStaff_toolButton.setMaximumSize(QSize(151, 121))
        self.addStaff_toolButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon2 = QIcon()
        icon2.addFile(u":/icons/icons/addStaff.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.addStaff_toolButton.setIcon(icon2)
        self.addStaff_toolButton.setIconSize(QSize(80, 80))
        self.addStaff_toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.addStaff_toolButton, 0, 0, 1, 1)

        self.camera_toolButton = QToolButton(adminPage)
        self.camera_toolButton.setObjectName(u"camera_toolButton")
        self.camera_toolButton.setMinimumSize(QSize(151, 121))
        self.camera_toolButton.setMaximumSize(QSize(151, 121))
        self.camera_toolButton.setStyleSheet(u"color: rgb(255, 255, 255);")
        icon3 = QIcon()
        icon3.addFile(u":/icons/icons/patientAdd.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.camera_toolButton.setIcon(icon3)
        self.camera_toolButton.setIconSize(QSize(80, 80))
        self.camera_toolButton.setToolButtonStyle(Qt.ToolButtonStyle.ToolButtonTextUnderIcon)

        self.gridLayout.addWidget(self.camera_toolButton, 1, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 1, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(14, 292, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 0, 1, 1, 1)


        self.retranslateUi(adminPage)

        QMetaObject.connectSlotsByName(adminPage)
    # setupUi

    def retranslateUi(self, adminPage):
        adminPage.setWindowTitle(QCoreApplication.translate("adminPage", u"Form", None))
        self.logout_toolButton.setText(QCoreApplication.translate("adminPage", u"Exit", None))
        self.viewData_toolButton.setText(QCoreApplication.translate("adminPage", u"Data", None))
        self.addStaff_toolButton.setText(QCoreApplication.translate("adminPage", u"Add", None))
        self.camera_toolButton.setText(QCoreApplication.translate("adminPage", u"Patient", None))
    # retranslateUi


