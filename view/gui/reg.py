# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reg.ui'
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
        self.btnReturn.setGeometry(QRect(400, 360, 380, 80))
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
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(10, 10, 191, 61))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(200, 70, 191, 61))
        self.label_4.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_5 = QLabel(self.frame)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(200, 140, 191, 61))
        self.label_5.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(200, 220, 191, 61))
        self.label_6.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.nameLine = QLineEdit(self.frame)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setGeometry(QRect(390, 80, 230, 40))
        self.nameLine.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.modeLine = QLineEdit(self.frame)
        self.modeLine.setObjectName(u"modeLine")
        self.modeLine.setGeometry(QRect(390, 150, 230, 40))
        self.modeLine.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")
        self.serialLine = QLineEdit(self.frame)
        self.serialLine.setObjectName(u"serialLine")
        self.serialLine.setGeometry(QRect(390, 230, 230, 40))
        self.serialLine.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"background-color:rgba(0,0,0,255);\n"
"color: rgb(255,255,255);\n"
"}")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u4eea\u5668\u8bbe\u7f6e", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u4eea\u5668\u540d\u79f0", None))
        self.label_5.setText(QCoreApplication.translate("Form", u"\u4eea\u5668\u578b\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u4eea\u5668\u6279\u53f7", None))
    # retranslateUi

