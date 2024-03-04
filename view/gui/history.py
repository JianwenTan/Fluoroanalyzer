# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'history.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *


class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(800, 450)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 350))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 211, 51))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.dateBox = QDateEdit(self.page)
        self.dateBox.setObjectName(u"dateBox")
        self.dateBox.setGeometry(QRect(190, 80, 230, 70))
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.dateBox.sizePolicy().hasHeightForWidth())
        self.dateBox.setSizePolicy(sizePolicy)
        self.dateBox.setStyleSheet(u"QDateEdit {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QDateEdit::drop-down\n"
"{\n"
"width:56px;  height:56px;\n"
"}\n"
"\n"
"\n"
"QCalendarWidget{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(5, 171, 194);\n"
"}\n"
"\n"
"QCalendarWidget QAbstractItemView:enabled{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(5, 171, 194);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(5, 171, 194);\n"
"}\n"
"\n"
"QCalendarWidget QToolButton QMenu{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(5, 171, 194);\n"
"}\n"
"\n"
"QCalendarWidget QSpinBox#qt_calendar_yearedit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background:#05abc2;\n"
"height:34px;\n"
"width:125px;\n"
"selection-background-color:#05abc2;\n"
"}\n"
"QCalendarWidget QSpinBox::up-butt"
                        "on \n"
"{ subcontrol-origin: border;  subcontrol-position: top right;  width:65px; }\n"
"QCalendarWidget QSpinBox::down-button\n"
" {subcontrol-origin: border; subcontrol-position: bottom right;  width:65px;}\n"
"QCalendarWidget QSpinBox::up-arrow\n"
" { width:56px;  height:56px; }\n"
"QCalendarWidget QSpinBox::down-arrow\n"
" { width:56px;  height:56px; }")
        self.dateBox.setButtonSymbols(QAbstractSpinBox.UpDownArrows)
        self.dateBox.setDateTime(QDateTime(QDate(2019, 12, 25), QTime(8, 0, 0)))
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 80, 136, 67))
        self.label_2.setMinimumSize(QSize(0, 0))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.modeBox_3 = QComboBox(self.page)
        self.modeBox_3.setObjectName(u"modeBox_3")
        self.modeBox_3.setGeometry(QRect(190, 210, 230, 70))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.modeBox_3.sizePolicy().hasHeightForWidth())
        self.modeBox_3.setSizePolicy(sizePolicy1)
        self.modeBox_3.setStyleSheet(u"QComboBox::drop-down{\n"
"width:56px;  height:56px;\n"
"}\n"
"\n"
"QComboBox{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(0, 0, 0);/*\u80cc\u666f\u989c\u8272*/\n"
"    padding: 1px 2px 1px 2px;  /*\u9488\u5bf9\u4e8e\u7ec4\u5408\u6846\u4e2d\u7684\u6587\u672c\u5185\u5bb9*/\n"
"	color: rgb(255,255,255)\n"
"}")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 210, 161, 67))
        sizePolicy1.setHeightForWidth(self.label.sizePolicy().hasHeightForWidth())
        self.label.setSizePolicy(sizePolicy1)
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(430, 80, 111, 71))
        self.label_4.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(430, 210, 111, 71))
        self.label_5.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.lineEdit = QLineEdit(self.page)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(550, 80, 230, 71))
        self.lineEdit.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.lineEdit_2 = QLineEdit(self.page)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setGeometry(QRect(550, 210, 230, 71))
        self.lineEdit_2.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.historyTable = QTableView(self.page_2)
        self.historyTable.setObjectName(u"historyTable")
        self.historyTable.setGeometry(QRect(10, 0, 778, 350))
        sizePolicy1.setHeightForWidth(self.historyTable.sizePolicy().hasHeightForWidth())
        self.historyTable.setSizePolicy(sizePolicy1)
        self.historyTable.setStyleSheet(u"#historyTable {\n"
"		font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.picLabel = QLabel(self.page_3)
        self.picLabel.setObjectName(u"picLabel")
        self.picLabel.setGeometry(QRect(230, 10, 351, 331))
        self.picLabel.setStyleSheet(u"font: 60pt \"\u5e7c\u5706\";")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.tableWidget = QTableWidget(self.page_4)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 10, 771, 341))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QTableWidget::Item\n"
"{\n"
"border:2px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_4)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 350, 800, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnConfirm = QPushButton(self.frame)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setGeometry(QRect(10, 10, 380, 80))
        self.btnConfirm.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnReturn = QPushButton(self.frame)
        self.btnReturn.setObjectName(u"btnReturn")
        self.btnReturn.setGeometry(QRect(410, 10, 380, 80))
        self.btnReturn.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnPre = QPushButton(self.frame)
        self.btnPre.setObjectName(u"btnPre")
        self.btnPre.setGeometry(QRect(10, 10, 187, 80))
        self.btnPre.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnNext = QPushButton(self.frame)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(207, 10, 187, 80))
        self.btnNext.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnDetail = QPushButton(self.frame)
        self.btnDetail.setObjectName(u"btnDetail")
        self.btnDetail.setGeometry(QRect(404, 10, 187, 80))
        self.btnDetail.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnReport = QPushButton(self.frame)
        self.btnReport.setObjectName(u"btnReport")
        self.btnReport.setGeometry(QRect(404, 10, 187, 80))
        self.btnReport.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnPrint = QPushButton(self.frame)
        self.btnPrint.setObjectName(u"btnPrint")
        self.btnPrint.setGeometry(QRect(207, 10, 187, 80))
        self.btnPrint.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnDownload = QPushButton(self.frame)
        self.btnDownload.setObjectName(u"btnDownload")
        self.btnDownload.setGeometry(QRect(10, 10, 187, 80))
        self.btnDownload.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5386\u53f2\u8bb0\u5f55\u67e5\u8be2", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u65f6\u95f4*", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u7ec4\u5408*", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u9001\u68c0\u533b\u751f", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u79d1\u5ba4", None))
        self.picLabel.setText("")
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.btnPre.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u7ec4", None))
        self.btnNext.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u7ec4", None))
        self.btnDetail.setText(QCoreApplication.translate("Form", u"\u8be6\u60c5", None))
        self.btnReport.setText(QCoreApplication.translate("Form", u"\u62a5\u544a\u5355", None))
        self.btnPrint.setText(QCoreApplication.translate("Form", u"\u6253\u5370", None))
        self.btnDownload.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
    # retranslateUi

