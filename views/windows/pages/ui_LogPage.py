# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'LogPagexzrwWg.ui'
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
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)

class Ui_LogPage(object):
    def setupUi(self, LogPage):
        if not LogPage.objectName():
            LogPage.setObjectName(u"LogPage")
        LogPage.resize(951, 880)
        self.gridLayout = QGridLayout(LogPage)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setVerticalSpacing(20)
        self.gridLayout.setContentsMargins(30, 30, 30, 30)
        self.logs_tableWidget = QTableWidget(LogPage)
        if (self.logs_tableWidget.columnCount() < 9):
            self.logs_tableWidget.setColumnCount(9)
        __qtablewidgetitem = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(7, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.logs_tableWidget.setHorizontalHeaderItem(8, __qtablewidgetitem8)
        self.logs_tableWidget.setObjectName(u"logs_tableWidget")
        self.logs_tableWidget.horizontalHeader().setDefaultSectionSize(100)
        self.logs_tableWidget.horizontalHeader().setStretchLastSection(True)

        self.gridLayout.addWidget(self.logs_tableWidget, 0, 0, 1, 1)


        self.retranslateUi(LogPage)

        QMetaObject.connectSlotsByName(LogPage)
    # setupUi

    def retranslateUi(self, LogPage):
        LogPage.setWindowTitle(QCoreApplication.translate("LogPage", u"Form", None))
        ___qtablewidgetitem = self.logs_tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("LogPage", u"ID", None));
        ___qtablewidgetitem1 = self.logs_tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("LogPage", u"Drawer Number", None));
        ___qtablewidgetitem2 = self.logs_tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("LogPage", u"Drawer Slot", None));
        ___qtablewidgetitem3 = self.logs_tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("LogPage", u"Staff ID", None));
        ___qtablewidgetitem4 = self.logs_tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("LogPage", u"Medicine", None));
        ___qtablewidgetitem5 = self.logs_tableWidget.horizontalHeaderItem(5)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("LogPage", u"Quantity", None));
        ___qtablewidgetitem6 = self.logs_tableWidget.horizontalHeaderItem(6)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("LogPage", u"Opened Date", None));
        ___qtablewidgetitem7 = self.logs_tableWidget.horizontalHeaderItem(7)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("LogPage", u"Closed Date", None));
        ___qtablewidgetitem8 = self.logs_tableWidget.horizontalHeaderItem(8)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("LogPage", u"Patient", None));
    # retranslateUi

