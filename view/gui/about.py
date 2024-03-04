# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'about.ui'
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
        self.label_36 = QLabel(self.frame)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setGeometry(QRect(510, 110, 221, 60))
        self.label_36.setStyleSheet(u"font: 20pt \"Times New Roman\";")
        self.label_35 = QLabel(self.frame)
        self.label_35.setObjectName(u"label_35")
        self.label_35.setGeometry(QRect(180, 110, 121, 60))
        self.label_35.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_3 = QLabel(self.frame)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(0, 0, 121, 41))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
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
        self.btnUpload = QPushButton(self.frame)
        self.btnUpload.setObjectName(u"btnUpload")
        self.btnUpload.setGeometry(QRect(10, 360, 380, 80))
        self.btnUpload.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(180, 220, 141, 60))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.version_label = QLabel(self.frame)
        self.version_label.setObjectName(u"version_label")
        self.version_label.setGeometry(QRect(360, 220, 311, 60))
        self.version_label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(360, 110, 151, 60))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label_36.setText(QCoreApplication.translate("Form", u"CIO-1001", None))
        self.label_35.setText(QCoreApplication.translate("Form", u"\u4eea\u5668\u578b\u53f7", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u5173\u4e8e\u4eea\u5668", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.btnUpload.setText(QCoreApplication.translate("Form", u"\u4e0a\u4f20", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u8f6f\u4ef6\u7248\u672c\u53f7", None))
        self.version_label.setText(QCoreApplication.translate("Form", u"V1.0.1", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8367\u5149\u5206\u6790\u4eea", None))
    # retranslateUi

