# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'CreatePatientPageqTqnUl.ui'
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
    QHBoxLayout, QLabel, QLineEdit, QPlainTextEdit,
    QPushButton, QSizePolicy, QSpacerItem, QVBoxLayout,
    QWidget)

class Ui_CreatePatientPage(object):
    def setupUi(self, CreatePatientPage):
        if not CreatePatientPage.objectName():
            CreatePatientPage.setObjectName(u"CreatePatientPage")
        CreatePatientPage.resize(598, 509)
        self.gridLayout = QGridLayout(CreatePatientPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_5 = QVBoxLayout()
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(-1, -1, -1, 0)
        self.label_3 = QLabel(CreatePatientPage)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMinimumSize(QSize(60, 20))
        self.label_3.setMaximumSize(QSize(60, 20))

        self.verticalLayout_3.addWidget(self.label_3)

        self.name_lineEdit = QLineEdit(CreatePatientPage)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setMinimumSize(QSize(150, 22))
        self.name_lineEdit.setMaximumSize(QSize(150, 22))
        self.name_lineEdit.setMaxLength(50)
        self.name_lineEdit.setFrame(False)

        self.verticalLayout_3.addWidget(self.name_lineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout_3)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(-1, -1, -1, 0)
        self.label_7 = QLabel(CreatePatientPage)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(60, 20))
        self.label_7.setMaximumSize(QSize(60, 20))

        self.verticalLayout_7.addWidget(self.label_7)

        self.contact_lineEdit = QLineEdit(CreatePatientPage)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")
        self.contact_lineEdit.setMinimumSize(QSize(150, 22))
        self.contact_lineEdit.setMaximumSize(QSize(150, 22))
        self.contact_lineEdit.setMaxLength(50)
        self.contact_lineEdit.setFrame(False)

        self.verticalLayout_7.addWidget(self.contact_lineEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout_7)

        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, -1, 0)
        self.label_5 = QLabel(CreatePatientPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMaximumSize(QSize(60, 20))

        self.verticalLayout_6.addWidget(self.label_5)

        self.gender_ComboBox = QComboBox(CreatePatientPage)
        self.gender_ComboBox.addItem("")
        self.gender_ComboBox.addItem("")
        self.gender_ComboBox.setObjectName(u"gender_ComboBox")
        self.gender_ComboBox.setMinimumSize(QSize(150, 0))
        self.gender_ComboBox.setMaximumSize(QSize(150, 22))

        self.verticalLayout_6.addWidget(self.gender_ComboBox)


        self.verticalLayout_2.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(-1, -1, -1, 0)
        self.label_4 = QLabel(CreatePatientPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(60, 20))
        self.label_4.setMaximumSize(QSize(60, 20))

        self.verticalLayout_4.addWidget(self.label_4)

        self.date_dateEdit = QDateEdit(CreatePatientPage)
        self.date_dateEdit.setObjectName(u"date_dateEdit")
        self.date_dateEdit.setMinimumSize(QSize(150, 22))
        self.date_dateEdit.setMaximumSize(QSize(150, 22))
        self.date_dateEdit.setFrame(False)

        self.verticalLayout_4.addWidget(self.date_dateEdit)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.horizontalLayout.addLayout(self.verticalLayout_2)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer)

        self.label = QLabel(CreatePatientPage)
        self.label.setObjectName(u"label")

        self.verticalLayout.addWidget(self.label)

        self.medicalHistory_plainTextEdit = QPlainTextEdit(CreatePatientPage)
        self.medicalHistory_plainTextEdit.setObjectName(u"medicalHistory_plainTextEdit")
        self.medicalHistory_plainTextEdit.setMinimumSize(QSize(256, 192))
        self.medicalHistory_plainTextEdit.setMaximumSize(QSize(256, 192))

        self.verticalLayout.addWidget(self.medicalHistory_plainTextEdit)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.verticalLayout.addItem(self.verticalSpacer_2)


        self.horizontalLayout.addLayout(self.verticalLayout)


        self.verticalLayout_5.addLayout(self.horizontalLayout)

        self.add_pushButton = QPushButton(CreatePatientPage)
        self.add_pushButton.setObjectName(u"add_pushButton")
        self.add_pushButton.setMinimumSize(QSize(30, 50))
        self.add_pushButton.setStyleSheet(u"background-color: rgb(0, 173, 181);\n"
"font: 700 12pt \"Segoe UI\";")

        self.verticalLayout_5.addWidget(self.add_pushButton)


        self.gridLayout.addLayout(self.verticalLayout_5, 0, 0, 1, 1)


        self.retranslateUi(CreatePatientPage)

        QMetaObject.connectSlotsByName(CreatePatientPage)
    # setupUi

    def retranslateUi(self, CreatePatientPage):
        CreatePatientPage.setWindowTitle(QCoreApplication.translate("CreatePatientPage", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("CreatePatientPage", u"Name", None))
        self.name_lineEdit.setInputMask("")
        self.label_7.setText(QCoreApplication.translate("CreatePatientPage", u"contact", None))
        self.contact_lineEdit.setInputMask("")
        self.label_5.setText(QCoreApplication.translate("CreatePatientPage", u"Gender", None))
        self.gender_ComboBox.setItemText(0, QCoreApplication.translate("CreatePatientPage", u"M", None))
        self.gender_ComboBox.setItemText(1, QCoreApplication.translate("CreatePatientPage", u"F", None))

        self.label_4.setText(QCoreApplication.translate("CreatePatientPage", u"Birth Date", None))
        self.label.setText(QCoreApplication.translate("CreatePatientPage", u"Medical History:", None))
        self.add_pushButton.setText(QCoreApplication.translate("CreatePatientPage", u"Add", None))
    # retranslateUi

