# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ViewPatientPageQxUdaX.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHBoxLayout, QLabel,
    QLineEdit, QSizePolicy, QSpacerItem, QTextEdit,
    QVBoxLayout, QWidget)

class Ui_ViewPatientPage(object):
    def setupUi(self, ViewPatientPage):
        if not ViewPatientPage.objectName():
            ViewPatientPage.setObjectName(u"ViewPatientPage")
        ViewPatientPage.resize(887, 654)
        self.gridLayout = QGridLayout(ViewPatientPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.viewPatientPage = QWidget(ViewPatientPage)
        self.viewPatientPage.setObjectName(u"viewPatientPage")
        self.gridLayout_2 = QGridLayout(self.viewPatientPage)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(15)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.viewPatientPage)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.name_lineEdit = QLineEdit(self.viewPatientPage)
        self.name_lineEdit.setObjectName(u"name_lineEdit")
        self.name_lineEdit.setEnabled(True)
        self.name_lineEdit.setMinimumSize(QSize(200, 0))
        self.name_lineEdit.setMaximumSize(QSize(200, 16777215))
        self.name_lineEdit.setReadOnly(True)

        self.horizontalLayout.addWidget(self.name_lineEdit, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout.addItem(self.horizontalSpacer_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.viewPatientPage)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(55, 0))

        self.horizontalLayout_4.addWidget(self.label_5, 0, Qt.AlignmentFlag.AlignHCenter)

        self.contact_lineEdit = QLineEdit(self.viewPatientPage)
        self.contact_lineEdit.setObjectName(u"contact_lineEdit")
        self.contact_lineEdit.setMinimumSize(QSize(150, 0))
        self.contact_lineEdit.setMaximumSize(QSize(150, 16777215))
        self.contact_lineEdit.setReadOnly(True)

        self.horizontalLayout_4.addWidget(self.contact_lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.viewPatientPage)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.date_lineEdit = QLineEdit(self.viewPatientPage)
        self.date_lineEdit.setObjectName(u"date_lineEdit")
        self.date_lineEdit.setMinimumSize(QSize(116, 22))
        self.date_lineEdit.setMaximumSize(QSize(116, 22))
        self.date_lineEdit.setReadOnly(True)

        self.horizontalLayout_2.addWidget(self.date_lineEdit, 0, Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignVCenter)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer_4)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.viewPatientPage)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3, 0, Qt.AlignmentFlag.AlignHCenter)

        self.gender_lineEdit = QLineEdit(self.viewPatientPage)
        self.gender_lineEdit.setObjectName(u"gender_lineEdit")
        self.gender_lineEdit.setMinimumSize(QSize(50, 0))
        self.gender_lineEdit.setMaximumSize(QSize(50, 16777215))
        self.gender_lineEdit.setReadOnly(True)

        self.horizontalLayout_3.addWidget(self.gender_lineEdit, 0, Qt.AlignmentFlag.AlignHCenter)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer_6)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setSpacing(15)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_4 = QLabel(self.viewPatientPage)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMinimumSize(QSize(290, 16))
        self.label_4.setMaximumSize(QSize(290, 16))
        self.label_4.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.verticalLayout.addWidget(self.label_4, 0, Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignVCenter)

        self.textEdit = QTextEdit(self.viewPatientPage)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setMinimumSize(QSize(300, 200))
        self.textEdit.setMaximumSize(QSize(300, 200))
        self.textEdit.setReadOnly(True)

        self.verticalLayout.addWidget(self.textEdit, 0, Qt.AlignmentFlag.AlignLeft)


        self.verticalLayout_2.addLayout(self.verticalLayout)


        self.gridLayout_2.addLayout(self.verticalLayout_2, 1, 1, 1, 1)

        self.horizontalSpacer = QSpacerItem(264, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer, 1, 2, 1, 1)

        self.verticalSpacer_2 = QSpacerItem(20, 105, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_2, 0, 1, 1, 1)

        self.verticalSpacer_3 = QSpacerItem(20, 104, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding)

        self.gridLayout_2.addItem(self.verticalSpacer_3, 2, 1, 1, 1)

        self.horizontalSpacer_3 = QSpacerItem(265, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)

        self.gridLayout_2.addItem(self.horizontalSpacer_3, 1, 0, 1, 1)

        self.widget = QWidget(self.viewPatientPage)
        self.widget.setObjectName(u"widget")

        self.gridLayout_2.addWidget(self.widget, 0, 0, 1, 1)


        self.gridLayout.addWidget(self.viewPatientPage, 0, 0, 1, 1)


        self.retranslateUi(ViewPatientPage)

        QMetaObject.connectSlotsByName(ViewPatientPage)
    # setupUi

    def retranslateUi(self, ViewPatientPage):
        ViewPatientPage.setWindowTitle(QCoreApplication.translate("ViewPatientPage", u"Form", None))
        self.label.setText(QCoreApplication.translate("ViewPatientPage", u"Name: ", None))
        self.name_lineEdit.setText(QCoreApplication.translate("ViewPatientPage", u"Helloo", None))
        self.label_5.setText(QCoreApplication.translate("ViewPatientPage", u"Contact:", None))
        self.label_2.setText(QCoreApplication.translate("ViewPatientPage", u"Birth Date:", None))
        self.label_3.setText(QCoreApplication.translate("ViewPatientPage", u"Gender: ", None))
        self.label_4.setText(QCoreApplication.translate("ViewPatientPage", u"Medical History:", None))
    # retranslateUi

