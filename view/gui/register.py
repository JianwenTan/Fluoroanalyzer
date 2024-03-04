# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'register.ui'
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
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 120, 50))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(190, 80, 121, 67))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 170, 121, 67))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_4 = QLabel(self.frame)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(190, 250, 121, 67))
        self.label_4.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.nameLine = QLineEdit(self.frame)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setGeometry(QRect(400, 70, 230, 70))
        self.nameLine.setStyleSheet(u"\n"
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
        self.pwdLine = QLineEdit(self.frame)
        self.pwdLine.setObjectName(u"pwdLine")
        self.pwdLine.setGeometry(QRect(400, 160, 230, 70))
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
        self.pwdLine_2 = QLineEdit(self.frame)
        self.pwdLine_2.setObjectName(u"pwdLine_2")
        self.pwdLine_2.setGeometry(QRect(400, 250, 230, 70))
        self.pwdLine_2.setStyleSheet(u"\n"
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c\u7528\u6237", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u65b0\u5bc6\u7801", None))
        self.label_4.setText(QCoreApplication.translate("Form", u"\u518d\u6b21\u8f93\u5165", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi

