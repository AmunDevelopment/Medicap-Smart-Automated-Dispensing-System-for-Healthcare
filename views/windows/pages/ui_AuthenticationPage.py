# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'AuthenticationPageDXfIiQ.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QLabel, QSizePolicy,
    QWidget)

class Ui_authenticationPage(object):
    def setupUi(self, authenticationPage):
        if not authenticationPage.objectName():
            authenticationPage.setObjectName(u"authenticationPage")
        authenticationPage.resize(598, 422)
        authenticationPage.setMinimumSize(QSize(598, 422))
        self.gridLayout = QGridLayout(authenticationPage)
        self.gridLayout.setSpacing(0)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.cameraCaptureLabel = QLabel(authenticationPage)
        self.cameraCaptureLabel.setObjectName(u"cameraCaptureLabel")
        self.cameraCaptureLabel.setMinimumSize(QSize(598, 422))
        self.cameraCaptureLabel.setStyleSheet(u"background-color: rgb(255, 255, 255);")

        self.gridLayout.addWidget(self.cameraCaptureLabel, 0, 0, 1, 1)


        self.retranslateUi(authenticationPage)

        QMetaObject.connectSlotsByName(authenticationPage)
    # setupUi

    def retranslateUi(self, authenticationPage):
        authenticationPage.setWindowTitle(QCoreApplication.translate("authenticationPage", u"Form", None))
        self.cameraCaptureLabel.setText("")
    # retranslateUi

