# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login.ui'
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
        self.frame_3 = QFrame(self.frame)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setGeometry(QRect(0, 0, 800, 450))
        self.frame_3.setFrameShape(QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Raised)
        self.registerBtn = QPushButton(self.frame_3)
        self.registerBtn.setObjectName(u"registerBtn")
        self.registerBtn.setGeometry(QRect(150, 280, 220, 80))
        self.registerBtn.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.loginBtn = QPushButton(self.frame_3)
        self.loginBtn.setObjectName(u"loginBtn")
        self.loginBtn.setGeometry(QRect(500, 280, 220, 80))
        self.loginBtn.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"border-radius: 35px;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.label = QLabel(self.frame_3)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(130, 80, 230, 70))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 160, 230, 70))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.nameLine = QLineEdit(self.frame_3)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setGeometry(QRect(360, 80, 230, 70))
        self.nameLine.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255,255,255);\n"
"background-color:rgba(0,0,0,255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
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
        self.numLine = QLineEdit(self.frame_3)
        self.numLine.setObjectName(u"numLine")
        self.numLine.setGeometry(QRect(360, 160, 230, 70))
        self.numLine.setStyleSheet(u"QLineEdit{\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255,255,255);\n"
"background-color:rgba(0,0,0,255);\n"
"border:none;\n"
"border-bottom:2px solid rgba(0,0,0,255);\n"
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
        self.register_icon_label = QLabel(self.frame_3)
        self.register_icon_label.setObjectName(u"register_icon_label")
        self.register_icon_label.setGeometry(QRect(150, 280, 80, 80))
        self.register_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.login_icon_label = QLabel(self.frame_3)
        self.login_icon_label.setObjectName(u"login_icon_label")
        self.login_icon_label.setGeometry(QRect(500, 280, 80, 80))
        self.login_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.registerBtn.setText(QCoreApplication.translate("Form", u"\u6ce8\u518c", None))
        self.loginBtn.setText(QCoreApplication.translate("Form", u"\u767b\u5f55", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u5bc6\u7801", None))
        self.register_icon_label.setText("")
        self.login_icon_label.setText("")
    # retranslateUi

