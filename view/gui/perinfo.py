# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'perinfo.ui'
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
        self.frame.setGeometry(QRect(0, 0, 800, 350))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(70, 50, 121, 51))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton = QRadioButton(self.frame)
        self.radioButton.setObjectName(u"radioButton")
        self.radioButton.setGeometry(QRect(160, 130, 220, 51))
        self.radioButton.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton.setAutoExclusive(False)
        self.radioButton_2 = QRadioButton(self.frame)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(430, 130, 220, 51))
        self.radioButton_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton_2.setAutoExclusive(False)
        self.radioButton_3 = QRadioButton(self.frame)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(160, 190, 220, 51))
        self.radioButton_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton_3.setAutoExclusive(False)
        self.radioButton_4 = QRadioButton(self.frame)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(430, 190, 220, 51))
        self.radioButton_4.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton_4.setAutoExclusive(False)
        self.radioButton_5 = QRadioButton(self.frame)
        self.radioButton_5.setObjectName(u"radioButton_5")
        self.radioButton_5.setGeometry(QRect(160, 250, 220, 51))
        self.radioButton_5.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton_5.setAutoExclusive(False)
        self.radioButton_6 = QRadioButton(self.frame)
        self.radioButton_6.setObjectName(u"radioButton_6")
        self.radioButton_6.setGeometry(QRect(430, 250, 220, 51))
        self.radioButton_6.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.radioButton_6.setAutoExclusive(False)
        self.frame_2 = QFrame(Form)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(0, 350, 800, 100))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.btnPre = QPushButton(self.frame_2)
        self.btnPre.setObjectName(u"btnPre")
        self.btnPre.setGeometry(QRect(10, 10, 187, 80))
        self.btnPre.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")
        self.btnReturn = QPushButton(self.frame_2)
        self.btnReturn.setObjectName(u"btnReturn")
        self.btnReturn.setGeometry(QRect(601, 10, 187, 80))
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
        self.btnConfirm = QPushButton(self.frame_2)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setGeometry(QRect(404, 10, 187, 80))
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
        self.btnNext = QPushButton(self.frame_2)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(207, 10, 187, 80))
        self.btnNext.setStyleSheet(u"QPushButton {\n"
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
        self.label.setText(QCoreApplication.translate("Form", u"\u7528\u6237\u540d1", None))
        self.radioButton.setText(QCoreApplication.translate("Form", u"\u8367\u5149\u68c0\u75ab\u64cd\u4f5c", None))
        self.radioButton_2.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u68c0\u75ab\u8bbe\u7f6e", None))
        self.radioButton_3.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u5386\u53f2\u8bb0\u5f55", None))
        self.radioButton_4.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u68c0\u6d4b\u8bbe\u7f6e", None))
        self.radioButton_5.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u5386\u53f2\u8bb0\u5f55", None))
        self.radioButton_6.setText(QCoreApplication.translate("Form", u"\u67e5\u770b\u7cfb\u7edf\u8bbe\u7f6e", None))
        self.btnPre.setText(QCoreApplication.translate("Form", u"\u4e0a\u4e00\u9875", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnNext.setText(QCoreApplication.translate("Form", u"\u4e0b\u4e00\u9875", None))
    # retranslateUi

