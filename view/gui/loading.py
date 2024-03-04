# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'loading.ui'
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
        Form.resize(800, 480)
        Form.setStyleSheet(u"background-color: rgb(255, 255, 255);")
        self.topframe = QFrame(Form)
        self.topframe.setObjectName(u"topframe")
        self.topframe.setGeometry(QRect(0, 0, 800, 30))
        self.topframe.setFrameShape(QFrame.StyledPanel)
        self.topframe.setFrameShadow(QFrame.Raised)
        self.title_label = QLabel(self.topframe)
        self.title_label.setObjectName(u"title_label")
        self.title_label.setGeometry(QRect(0, 0, 200, 30))
        self.time_label = QLabel(self.topframe)
        self.time_label.setObjectName(u"time_label")
        self.time_label.setGeometry(QRect(600, 0, 200, 30))
        self.wifi_label = QLabel(self.topframe)
        self.wifi_label.setObjectName(u"wifi_label")
        self.wifi_label.setGeometry(QRect(550, 0, 30, 30))
        self.centerframe = QFrame(Form)
        self.centerframe.setObjectName(u"centerframe")
        self.centerframe.setGeometry(QRect(0, 30, 800, 450))
        self.centerframe.setFrameShape(QFrame.StyledPanel)
        self.centerframe.setFrameShadow(QFrame.Raised)
        self.textEdit = QTextEdit(self.centerframe)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setGeometry(QRect(70, 30, 680, 291))
        self.textEdit.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.btnRetry = QPushButton(self.centerframe)
        self.btnRetry.setObjectName(u"btnRetry")
        self.btnRetry.setGeometry(QRect(570, 330, 220, 80))
        self.btnRetry.setStyleSheet(u"QPushButton {\n"
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
        self.retry_icon_label = QLabel(self.centerframe)
        self.retry_icon_label.setObjectName(u"retry_icon_label")
        self.retry_icon_label.setGeometry(QRect(570, 330, 80, 80))
        self.retry_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
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
        self.title_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.time_label.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.wifi_label.setText("")
        self.btnRetry.setText(QCoreApplication.translate("Form", u"\u91cd\u8bd5", None))
        self.retry_icon_label.setText("")
    # retranslateUi

