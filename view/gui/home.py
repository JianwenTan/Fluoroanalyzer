# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'home.ui'
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
        self.history_icon_label = QLabel(self.frame)
        self.history_icon_label.setObjectName(u"history_icon_label")
        self.history_icon_label.setGeometry(QRect(410, 100, 80, 80))
        self.history_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.btnData = QPushButton(self.frame)
        self.btnData.setObjectName(u"btnData")
        self.btnData.setGeometry(QRect(100, 100, 280, 80))
        self.btnData.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"border-radius: 35px;\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.sys_icon_label = QLabel(self.frame)
        self.sys_icon_label.setObjectName(u"sys_icon_label")
        self.sys_icon_label.setGeometry(QRect(410, 220, 80, 80))
        self.sys_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.reagent_icon_label = QLabel(self.frame)
        self.reagent_icon_label.setObjectName(u"reagent_icon_label")
        self.reagent_icon_label.setGeometry(QRect(100, 100, 80, 80))
        self.reagent_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
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
"border-radius: 35px;\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnPower = QPushButton(self.frame)
        self.btnPower.setObjectName(u"btnPower")
        self.btnPower.setGeometry(QRect(10, 360, 780, 80))
        self.btnPower.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.reagent_set_icon_label = QLabel(self.frame)
        self.reagent_set_icon_label.setObjectName(u"reagent_set_icon_label")
        self.reagent_set_icon_label.setGeometry(QRect(100, 220, 80, 80))
        self.reagent_set_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.btnPara = QPushButton(self.frame)
        self.btnPara.setObjectName(u"btnPara")
        self.btnPara.setGeometry(QRect(410, 220, 280, 80))
        self.btnPara.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"border-radius: 35px;\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnHistory = QPushButton(self.frame)
        self.btnHistory.setObjectName(u"btnHistory")
        self.btnHistory.setGeometry(QRect(410, 100, 280, 80))
        self.btnHistory.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"border-radius: 35px;\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnData.raise_()
        self.reagent_icon_label.raise_()
        self.btnSet.raise_()
        self.btnPower.raise_()
        self.reagent_set_icon_label.raise_()
        self.btnHistory.raise_()
        self.btnPara.raise_()
        self.sys_icon_label.raise_()
        self.history_icon_label.raise_()

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.history_icon_label.setText("")
        self.btnData.setText(QCoreApplication.translate("Form", u"  \u8367\u5149\u68c0\u6d4b", None))
        self.sys_icon_label.setText("")
        self.reagent_icon_label.setText("")
        self.btnSet.setText(QCoreApplication.translate("Form", u"  \u68c0\u75ab\u8bbe\u7f6e", None))
        self.btnPower.setText(QCoreApplication.translate("Form", u"\u7535\u6e90", None))
        self.reagent_set_icon_label.setText("")
        self.btnPara.setText(QCoreApplication.translate("Form", u"  \u7cfb\u7edf\u8bbe\u7f6e", None))
        self.btnHistory.setText(QCoreApplication.translate("Form", u"  \u5386\u53f2\u8bb0\u5f55", None))
    # retranslateUi

