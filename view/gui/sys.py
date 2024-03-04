# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'sys.ui'
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
        self.wifi_icon_label = QLabel(self.frame)
        self.wifi_icon_label.setObjectName(u"wifi_icon_label")
        self.wifi_icon_label.setGeometry(QRect(100, 100, 80, 80))
        self.wifi_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 121, 51))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.clear_icon_label = QLabel(self.frame)
        self.clear_icon_label.setObjectName(u"clear_icon_label")
        self.clear_icon_label.setGeometry(QRect(410, 100, 80, 80))
        self.clear_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.btnSet = QPushButton(self.frame)
        self.btnSet.setObjectName(u"btnSet")
        self.btnSet.setGeometry(QRect(100, 220, 280, 80))
        self.btnSet.setStyleSheet(u"QPushButton {\n"
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
        self.btnClear = QPushButton(self.frame)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(410, 100, 280, 80))
        self.btnClear.setStyleSheet(u"QPushButton {\n"
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
        self.about_icon_label = QLabel(self.frame)
        self.about_icon_label.setObjectName(u"about_icon_label")
        self.about_icon_label.setGeometry(QRect(410, 220, 80, 80))
        self.about_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.btnWifi = QPushButton(self.frame)
        self.btnWifi.setObjectName(u"btnWifi")
        self.btnWifi.setGeometry(QRect(100, 100, 280, 80))
        self.btnWifi.setStyleSheet(u"QPushButton {\n"
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
        self.btnAbout = QPushButton(self.frame)
        self.btnAbout.setObjectName(u"btnAbout")
        self.btnAbout.setGeometry(QRect(410, 220, 280, 80))
        self.btnAbout.setStyleSheet(u"QPushButton {\n"
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
        self.camera_icon_label = QLabel(self.frame)
        self.camera_icon_label.setObjectName(u"camera_icon_label")
        self.camera_icon_label.setGeometry(QRect(100, 220, 80, 80))
        self.camera_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.btnReturn = QPushButton(self.frame)
        self.btnReturn.setObjectName(u"btnReturn")
        self.btnReturn.setGeometry(QRect(10, 360, 780, 80))
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
        self.label.raise_()
        self.btnSet.raise_()
        self.btnClear.raise_()
        self.btnWifi.raise_()
        self.btnAbout.raise_()
        self.about_icon_label.raise_()
        self.camera_icon_label.raise_()
        self.clear_icon_label.raise_()
        self.wifi_icon_label.raise_()
        self.btnReturn.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.wifi_icon_label.setText("")
        self.label.setText(QCoreApplication.translate("Form", u"\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.clear_icon_label.setText("")
        self.btnSet.setText(QCoreApplication.translate("Form", u"   \u8d28\u91cf\u63a7\u5236", None))
        self.btnClear.setText(QCoreApplication.translate("Form", u"  \u6e05\u9664\u7f13\u5b58", None))
        self.about_icon_label.setText("")
        self.btnWifi.setText(QCoreApplication.translate("Form", u"  wifi\u8bbe\u7f6e", None))
        self.btnAbout.setText(QCoreApplication.translate("Form", u"  \u5173\u4e8e\u4eea\u5668", None))
        self.camera_icon_label.setText("")
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi

