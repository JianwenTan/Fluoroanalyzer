# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'wifi.ui'
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
        self.frame.setGeometry(QRect(0, 0, 800, 450))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.wifiCb = QComboBox(self.frame)
        self.wifiCb.setObjectName(u"wifiCb")
        self.wifiCb.setGeometry(QRect(390, 70, 230, 70))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.wifiCb.sizePolicy().hasHeightForWidth())
        self.wifiCb.setSizePolicy(sizePolicy)
        self.wifiCb.setStyleSheet(u"QComboBox::drop-down{\n"
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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(160, 70, 161, 73))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 170, 151, 73))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.pwdLine = QLineEdit(self.frame)
        self.pwdLine.setObjectName(u"pwdLine")
        self.pwdLine.setGeometry(QRect(390, 170, 230, 70))
        sizePolicy.setHeightForWidth(self.pwdLine.sizePolicy().hasHeightForWidth())
        self.pwdLine.setSizePolicy(sizePolicy)
        font = QFont()
        font.setFamily(u"\u5b8b\u4f53")
        font.setPointSize(20)
        font.setBold(False)
        font.setItalic(False)
        self.pwdLine.setFont(font)
        self.pwdLine.setStyleSheet(u"\n"
"QLineEdit{\n"
"background-color:rgba(0,0,0,255);\n"
"border:none;\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
"	color: rgb(255, 255, 255);\n"
"}\n"
"QLineEdit:hover {\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgba(0, 0, 0, 240);\n"
"}\n"
"QLineEdit:focus {\n"
"border:none;\n"
"border-bottom:2px solid rgba(46, 82, 101, 200);\n"
"color:rgb(0, 170, 190);\n"
"}")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 121, 41))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.btnConfirm = QPushButton(self.frame)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setGeometry(QRect(10, 360, 380, 80))
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
        self.btnReturn.setGeometry(QRect(410, 360, 380, 80))
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
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(160, 270, 150, 70))
        self.label_4.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.addr_Label = QLabel(self.frame)
        self.addr_Label.setObjectName(u"addr_Label")
        self.addr_Label.setGeometry(QRect(390, 270, 230, 70))
        self.addr_Label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"wifi", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"wifi\u8bbe\u7f6e", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u672c\u673aIP", None))
        self.addr_Label.setText(QCoreApplication.translate("Form", u"127.0.0.1", None))
    # retranslateUi

