# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'update.ui'
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
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 191, 61))
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
        self.btnRestart = QPushButton(self.frame)
        self.btnRestart.setObjectName(u"btnRestart")
        self.btnRestart.setGeometry(QRect(250, 140, 280, 80))
        self.btnRestart.setStyleSheet(u"QPushButton {\n"
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
        self.restart_icon_label = QLabel(self.frame)
        self.restart_icon_label.setObjectName(u"restart_icon_label")
        self.restart_icon_label.setGeometry(QRect(250, 140, 80, 80))
        self.restart_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
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
        self.label_3.setText(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u66f4\u65b0", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.btnRestart.setText(QCoreApplication.translate("Form", u"  \u8f6f\u4ef6\u91cd\u542f", None))
        self.restart_icon_label.setText("")
    # retranslateUi

