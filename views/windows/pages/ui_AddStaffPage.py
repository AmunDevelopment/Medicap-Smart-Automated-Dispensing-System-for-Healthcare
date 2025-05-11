
# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addStaffNDKWcP.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDateEdit, QGridLayout,
    QHBoxLayout, QLabel, QLineEdit, QPushButton,
    QSizePolicy, QSpacerItem, QVBoxLayout, QWidget)
import src.views.assets.resources_rc

class Ui_addStaffPage(object):
    def setupUi(self, addStaffPage):
        if not addStaffPage.objectName():
            addStaffPage.setObjectName(u"addStaffPage")
        addStaffPage.resize(598, 422)
        self.gridLayout = QGridLayout(addStaffPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 30, -1, -1)
        self.verticalLayout_8 = QVBoxLayout()
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setSpacing(30)
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout_8.addLayout(self.horizontalLayout)

        self.camera_label = QLabel(addStaffPage)
        self.camera_label.setObjectName(u"camera_label")
        self.camera_label.setMinimumSize(QSize(231, 161))
        self.camera_label.setMaximumSize(QSize(231, 161))
        self.camera_label.setStyleSheet(u"background-color: rgb(107, 107, 107);\n"
"border-radius:10px;")
        self.camera_label.setScaledContents(True)

        self.verticalLayout_8.addWidget(self.camera_label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.verticalLayout_2.addLayout(self.verticalLayout_8)

        self.capture_pushButton = QPushButton(addStaffPage)
        self.capture_pushButton.setObjectName(u"capture_pushButton")
        self.capture_pushButton.setMinimumSize(QSize(150, 50))
        self.capture_pushButton.setMaximumSize(QSize(150, 50))
        self.capture_pushButton.setStyleSheet(u"background-color: rgb(0, 173, 181);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_2.addWidget(self.capture_pushButton, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)

        self.verticalSpacer_4 = QSpacerItem(20, 63, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout.addItem(self.verticalSpacer_4, 1, 1, 1, 1)

        self.widget = QWidget(addStaffPage)
        self.widget.setObjectName(u"widget")
        self.widget.setStyleSheet(u"QWidget{\n"
"	font: 700 9pt \"Segoe UI\";\n"
"	\n"
"	color: rgb(0, 0, 0);\n"
"}\n"
"QComboBox{\n"
"	background-color:rgb(153, 153, 153);\n"
"}\n"
"QLineEdit{\n"
"	border-radius: 7px;\n"
"	background-color:rgb(153, 153, 153);\n"
"}\n"
"QDateEdit{\n"
"	background-color:rgb(153, 153, 153);\n"
"}\n"
"QPushButton{\n"
"	\n"
"	background-color: rgb(255, 170, 127);\n"
"}\n"
"")
        self.verticalLayout = QVBoxLayout(self.widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 20))
        self.label_3.setMaximumSize(QSize(60, 20))

        self.verticalLayout_3.addWidget(self.label_3)

        self.name_lineEdit = QLineEdit(self.widget)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMaxLength(50)
        self.name_lineEdit.setFrame(False)

        self.verticalLayout_3.addWidget(self.name_lineEdit)


        self.verticalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.label_7 = QLabel(self.widget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 20))
        self.label_7.setMaximumSize(QSize(60, 20))

        self.verticalLayout_7.addWidget(self.label_7)

        self.contact_lineEdit = QLineEdit(self.widget)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")
        self.contact_lineEdit.setMinimumSize(QSize(150, 22))
        self.contact_lineEdit.setMaxLength(50)
        self.contact_lineEdit.setFrame(False)

        self.verticalLayout_7.addWidget(self.contact_lineEdit)


        self.verticalLayout.addLayout(self.verticalLayout_7)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.label_4 = QLabel(self.widget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 20))
        self.label_4.setMaximumSize(QSize(60, 20))

        self.verticalLayout_4.addWidget(self.label_4)

        self.date_dateEdit = QDateEdit(self.widget)
        self.date_dateEdit.setObjectName(u"date_dateEdit")
        self.date_dateEdit.setMinimumSize(QSize(150, 22))
        self.date_dateEdit.setFrame(False)

        self.verticalLayout_4.addWidget(self.date_dateEdit)


        self.verticalLayout.addLayout(self.verticalLayout_4)

        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.label_6 = QLabel(self.widget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(60, 20))
        self.label_6.setMaximumSize(QSize(60, 20))

        self.verticalLayout_5.addWidget(self.label_6)

        self.role_ComboBox = QComboBox(self.widget)
        self.role_ComboBox.addItem("")
        self.role_ComboBox.addItem("")
        self.role_ComboBox.setObjectName(u"role_ComboBox")
        self.role_ComboBox.setMinimumSize(QSize(150, 22))

        self.verticalLayout_5.addWidget(self.role_ComboBox)


        self.verticalLayout.addLayout(self.verticalLayout_5)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_5 = QLabel(self.widget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 20))

        self.verticalLayout_6.addWidget(self.label_5)

        self.gender_ComboBox = QComboBox(self.widget)
        self.gender_ComboBox.addItem("")
        self.gender_ComboBox.addItem("")
        self.gender_ComboBox.setObjectName(u"gender_ComboBox")
        self.gender_ComboBox.setMinimumSize(QSize(150, 0))

        self.verticalLayout_6.addWidget(self.gender_ComboBox)


        self.verticalLayout.addLayout(self.verticalLayout_6)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.Add_PushButton = QPushButton(self.widget)
        self.Add_PushButton.setObjectName(u"Add_PushButton")
        self.Add_PushButton.setMinimumSize(QSize(81, 41))
        self.Add_PushButton.setMaximumSize(QSize(81, 41))
        self.Add_PushButton.setStyleSheet(u"background-color: rgb(0, 0, 0);\n"
"font: 900 12pt \"Segoe UI\";\n"
"color: rgb(255, 255, 255);")

        self.verticalLayout.addWidget(self.Add_PushButton, 0, Qt.AlignmentFlag.AlignRight)


        self.gridLayout.addWidget(self.widget, 0, 1, 1, 1)


        self.retranslateUi(addStaffPage)

        QMetaObject.connectSlotsByName(addStaffPage)
    # setupUi

    def retranslateUi(self, addStaffPage):
        addStaffPage.setWindowTitle(QCoreApplication.translate("addStaffPage", u"Form", None))
        self.camera_label.setText("")
        self.capture_pushButton.setText(QCoreApplication.translate("addStaffPage", u"Capture", None))
        self.label_3.setText(QCoreApplication.translate("addStaffPage", u"Name", None))
        self.name_lineEdit.setInputMask("")
        self.label_7.setText(QCoreApplication.translate("addStaffPage", u"contact", None))
        self.contact_lineEdit.setInputMask("")
        self.label_4.setText(QCoreApplication.translate("addStaffPage", u"Birth Date", None))
        self.label_6.setText(QCoreApplication.translate("addStaffPage", u"Role", None))
        self.role_ComboBox.setItemText(0, QCoreApplication.translate("addStaffPage", u"Nurse", None))
        self.role_ComboBox.setItemText(1, QCoreApplication.translate("addStaffPage", u"Doctor", None))

        self.label_5.setText(QCoreApplication.translate("addStaffPage", u"Gender", None))
        self.gender_ComboBox.setItemText(0, QCoreApplication.translate("addStaffPage", u"M", None))
        self.gender_ComboBox.setItemText(1, QCoreApplication.translate("addStaffPage", u"F", None))

        self.Add_PushButton.setText(QCoreApplication.translate("addStaffPage", u"Add", None))
    # retranslateUi

