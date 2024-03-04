# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'test.ui'
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
        self.btnExe = QPushButton(self.frame)
        self.btnExe.setObjectName(u"btnExe")
        self.btnExe.setGeometry(QRect(10, 10, 380, 80))
        self.btnExe.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnSwitch = QPushButton(self.frame)
        self.btnSwitch.setObjectName(u"btnSwitch")
        self.btnSwitch.setGeometry(QRect(404, 10, 187, 80))
        self.btnSwitch.setStyleSheet(u"QPushButton {\n"
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
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 350))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.paraLine = QLineEdit(self.page)
        self.paraLine.setObjectName(u"paraLine")
        self.paraLine.setGeometry(QRect(166, 150, 129, 31))
        self.paraLine.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.paraLine.setInputMethodHints(Qt.ImhDigitsOnly)
        self.label_4 = QLabel(self.page)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 294, 112, 27))
        self.label_4.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.pushButton_2 = QPushButton(self.page)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setEnabled(False)
        self.pushButton_2.setGeometry(QRect(19, 10, 271, 35))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setMaximumSize(QSize(16777215, 50))
        self.pushButton_2.setStyleSheet(u"background-color: rgb(5, 171, 194);\n"
"color: rgb(0, 0, 0);\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"")
        self.label_11 = QLabel(self.page)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(376, 294, 131, 40))
        self.label_11.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 261, 112, 27))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.ageLine = QLineEdit(self.page)
        self.ageLine.setObjectName(u"ageLine")
        self.ageLine.setGeometry(QRect(516, 134, 230, 40))
        self.ageLine.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.ageLine.setInputMethodHints(Qt.ImhDigitsOnly)
        self.nameLine = QLineEdit(self.page)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setGeometry(QRect(516, 84, 230, 40))
        self.nameLine.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.label_10 = QLabel(self.page)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(406, 244, 80, 40))
        self.label_10.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_6 = QLabel(self.page)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(406, 84, 80, 40))
        sizePolicy.setHeightForWidth(self.label_6.sizePolicy().hasHeightForWidth())
        self.label_6.setSizePolicy(sizePolicy)
        self.label_6.setMinimumSize(QSize(80, 40))
        self.label_6.setMaximumSize(QSize(80, 40))
        self.label_6.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_7 = QLabel(self.page)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 110, 140, 27))
        self.label_7.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"")
        self.pushButton_3 = QPushButton(self.page)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setEnabled(False)
        self.pushButton_3.setGeometry(QRect(19, 201, 271, 35))
        sizePolicy.setHeightForWidth(self.pushButton_3.sizePolicy().hasHeightForWidth())
        self.pushButton_3.setSizePolicy(sizePolicy)
        self.pushButton_3.setMaximumSize(QSize(16777215, 50))
        self.pushButton_3.setStyleSheet(u"background-color: rgb(5, 171, 194);\n"
"color: rgb(0, 0, 0);\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"")
        self.pushButton = QPushButton(self.page)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setEnabled(False)
        self.pushButton.setGeometry(QRect(346, 10, 441, 35))
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QSize(0, 0))
        self.pushButton.setMaximumSize(QSize(16777215, 50))
        self.pushButton.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color: rgb(5, 171, 194);\n"
"color: rgb(0, 0, 0);")
        self.label_5 = QLabel(self.page)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(169, 294, 112, 27))
        self.label_5.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_9 = QLabel(self.page)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(406, 189, 80, 40))
        self.label_9.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.modeBox_1 = QComboBox(self.page)
        self.modeBox_1.setObjectName(u"modeBox_1")
        self.modeBox_1.setGeometry(QRect(166, 67, 129, 31))
        self.modeBox_1.setStyleSheet(u"QComboBox::drop-down{\n"
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
        self.label_3 = QLabel(self.page)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 67, 140, 27))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"")
        self.label_2 = QLabel(self.page)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(169, 261, 112, 27))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.departCb = QLineEdit(self.page)
        self.departCb.setObjectName(u"departCb")
        self.departCb.setGeometry(QRect(516, 244, 230, 40))
        self.departCb.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.label_8 = QLabel(self.page)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(406, 134, 81, 51))
        self.label_8.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.docCb = QLineEdit(self.page)
        self.docCb.setObjectName(u"docCb")
        self.docCb.setGeometry(QRect(516, 294, 230, 40))
        self.docCb.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.label_12 = QLabel(self.page)
        self.label_12.setObjectName(u"label_12")
        self.label_12.setGeometry(QRect(20, 150, 140, 27))
        self.label_12.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.typeLabel = QLabel(self.page)
        self.typeLabel.setObjectName(u"typeLabel")
        self.typeLabel.setGeometry(QRect(166, 110, 129, 31))
        self.typeLabel.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton = QRadioButton(self.page)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(530, 190, 95, 40))
        self.radioButton.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton_2 = QRadioButton(self.page)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(650, 190, 95, 40))
        self.radioButton_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.exeTable = QTableView(self.page_2)
        self.exeTable.setObjectName(u"exeTable")
        self.exeTable.setGeometry(QRect(15, 0, 771, 350))
        self.exeTable.setStyleSheet(u"#exeTable{\n"
"	font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QComboBox {\n"
"    font: 20pt \"\u5b8b\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(0, 0, 0);/*\u80cc\u666f\u989c\u8272*/\n"
"    padding: 1px 2px 1px 2px;  /*\u9488\u5bf9\u4e8e\u7ec4\u5408\u6846\u4e2d\u7684\u6587\u672c\u5185\u5bb9*/\n"
"	color: rgb(255,255,255)\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.photoLabel = QLabel(self.page_3)
        self.photoLabel.setObjectName(u"photoLabel")
        self.photoLabel.setGeometry(QRect(440, 0, 350, 350))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.photoLabel.sizePolicy().hasHeightForWidth())
        self.photoLabel.setSizePolicy(sizePolicy1)
        self.photoLabel.setMinimumSize(QSize(350, 350))
        self.photoLabel.setMaximumSize(QSize(350, 350))
        self.photoLabel.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.photoLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.picLabel = QLabel(self.page_3)
        self.picLabel.setObjectName(u"picLabel")
        self.picLabel.setGeometry(QRect(10, 0, 350, 350))
        sizePolicy1.setHeightForWidth(self.picLabel.sizePolicy().hasHeightForWidth())
        self.picLabel.setSizePolicy(sizePolicy1)
        self.picLabel.setMinimumSize(QSize(350, 350))
        self.picLabel.setMaximumSize(QSize(350, 350))
        self.picLabel.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.picLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.leftLabel = QLabel(self.page_3)
        self.leftLabel.setObjectName(u"leftLabel")
        self.leftLabel.setGeometry(QRect(10, 0, 350, 30))
        self.leftLabel.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.rightLabel = QLabel(self.page_3)
        self.rightLabel.setObjectName(u"rightLabel")
        self.rightLabel.setGeometry(QRect(440, 0, 350, 30))
        self.rightLabel.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.stackedWidget.addWidget(self.page_3)
        self.photoLabel.raise_()
        self.picLabel.raise_()
        self.rightLabel.raise_()
        self.leftLabel.raise_()
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.tableView = QTableView(self.page_4)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(15, 0, 771, 350))
        self.tableView.setStyleSheet(u"QTableView {\n"
"	font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QComboBox {\n"
"    font: 20pt \"\u5b8b\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(0, 0, 0);/*\u80cc\u666f\u989c\u8272*/\n"
"    padding: 1px 2px 1px 2px;  /*\u9488\u5bf9\u4e8e\u7ec4\u5408\u6846\u4e2d\u7684\u6587\u672c\u5185\u5bb9*/\n"
"	color: rgb(255,255,255)\n"
"}")
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)

        self.stackedWidget.setCurrentIndex(3)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.btnExe.setText(QCoreApplication.translate("Form", u"\u5feb\u901f\u6d4b\u8bd5", None))
        self.btnSwitch.setText(QCoreApplication.translate("Form", u"\u5207\u6362", None))
        self.btnPrint.setText(QCoreApplication.translate("Form", u"\u6253\u5370", None))
        self.btnDownload.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u6279\u6b21\u7f16\u53f7", None))
        self.pushButton_2.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u4fe1\u606f", None))
        self.label_11.setText(QCoreApplication.translate("Form", u"\u9001\u68c0\u533b\u751f*", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u9879\u76ee", None))
        self.label_10.setText(QCoreApplication.translate("Form", u"\u79d1\u5ba4*", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u59d3\u540d*", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u89c4\u683c", None))
        self.pushButton_3.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u4fe1\u606f", None))
        self.pushButton.setText(QCoreApplication.translate("Form", u"\u75c5\u4eba\u4fe1\u606f", None))
        self.label_5.setText("")
        self.label_9.setText(QCoreApplication.translate("Form", u"\u6027\u522b*", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u68c0\u6d4b\u7ec4\u5408", None))
        self.label_2.setText("")
        self.label_8.setText(QCoreApplication.translate("Form", u"\u5e74\u9f84*", None))
        self.label_12.setText(QCoreApplication.translate("Form", u"\u53c2\u6570(\u9009\u586b)", None))
        self.typeLabel.setText("")
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u7537", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u5973", None))
        self.photoLabel.setText("")
        self.picLabel.setText(QCoreApplication.translate("Form", u"origin_photo", None))
        self.leftLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.rightLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

