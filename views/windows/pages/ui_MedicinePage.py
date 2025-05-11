# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MedicinePageFBbHbg.ui'
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
from PySide6.QtWidgets import (QApplication, QDoubleSpinBox, QGridLayout, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QScrollArea,
    QSizePolicy, QWidget)

class Ui_MedicinePage(object):
    def setupUi(self, MedicinePage):
        if not MedicinePage.objectName():
            MedicinePage.setObjectName(u"MedicinePage")
        MedicinePage.resize(598, 422)
        MedicinePage.setMinimumSize(QSize(598, 422))
        self.gridLayout = QGridLayout(MedicinePage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.lineEdit = QLineEdit(MedicinePage)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMinimumSize(QSize(340, 21))
        self.lineEdit.setMaximumSize(QSize(340, 21))

        self.horizontalLayout.addWidget(self.lineEdit)

        self.pushButton = QPushButton(MedicinePage)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(75, 24))

        self.horizontalLayout.addWidget(self.pushButton)

        self.reset_pushButton = QPushButton(MedicinePage)
        self.reset_pushButton.setObjectName(u"reset_pushButton")

        self.horizontalLayout.addWidget(self.reset_pushButton)


        self.gridLayout.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label = QLabel(MedicinePage)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)

        self.horizontalLayout_2.addWidget(self.label)

        self.quantity_doubleSpinBox = QDoubleSpinBox(MedicinePage)
        self.quantity_doubleSpinBox.setObjectName(u"quantity_doubleSpinBox")
        self.quantity_doubleSpinBox.setMinimumSize(QSize(81, 31))
        self.quantity_doubleSpinBox.setMaximumSize(QSize(81, 31))
        font1 = QFont()
        font1.setBold(True)
        self.quantity_doubleSpinBox.setFont(font1)
        self.quantity_doubleSpinBox.setDecimals(0)
        self.quantity_doubleSpinBox.setMinimum(1.000000000000000)
        self.quantity_doubleSpinBox.setMaximum(99.000000000000000)

        self.horizontalLayout_2.addWidget(self.quantity_doubleSpinBox, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)


        self.gridLayout.addLayout(self.horizontalLayout_2, 1, 0, 1, 1)

        self.scrollArea = QScrollArea(MedicinePage)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setMinimumSize(QSize(590, 300))
        self.scrollArea.setStyleSheet(u"QPushButton{\n"
"	min-width: 40px;\n"
"	min-height:30px;\n"
"	font: 700 10pt;\n"
"	background-color: rgb(0, 173, 181);\n"
"	\n"
"	color: rgb(57, 62, 70);\n"
"}\n"
"background-color: rgb(85, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 588, 331))
        self.buttons_gridLayout = QGridLayout(self.scrollAreaWidgetContents_2)
        self.buttons_gridLayout.setSpacing(8)
        self.buttons_gridLayout.setObjectName(u"buttons_gridLayout")
        self.buttons_gridLayout.setContentsMargins(0, 0, -1, 0)
        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.gridLayout.addWidget(self.scrollArea, 2, 0, 1, 1)


        self.retranslateUi(MedicinePage)

        QMetaObject.connectSlotsByName(MedicinePage)
    # setupUi

    def retranslateUi(self, MedicinePage):
        MedicinePage.setWindowTitle(QCoreApplication.translate("MedicinePage", u"Form", None))
        self.pushButton.setText(QCoreApplication.translate("MedicinePage", u"Search", None))
        self.reset_pushButton.setText(QCoreApplication.translate("MedicinePage", u"reset", None))
        self.label.setText(QCoreApplication.translate("MedicinePage", u"Quantity:", None))
    # retranslateUi

