# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'clear.ui'
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
        self.label.setGeometry(QRect(120, 240, 272, 67))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.clearBar = QProgressBar(self.frame)
        self.clearBar.setObjectName(u"clearBar")
        self.clearBar.setGeometry(QRect(130, 70, 611, 131))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.clearBar.sizePolicy().hasHeightForWidth())
        self.clearBar.setSizePolicy(sizePolicy)
        self.clearBar.setStyleSheet(u"font: 50pt \"\u5e7c\u5706\";\n"
"")
        self.clearBar.setValue(24)
        self.clearCb = QComboBox(self.frame)
        self.clearCb.setObjectName(u"clearCb")
        self.clearCb.setGeometry(QRect(460, 240, 230, 70))
        sizePolicy.setHeightForWidth(self.clearCb.sizePolicy().hasHeightForWidth())
        self.clearCb.setSizePolicy(sizePolicy)
        self.clearCb.setStyleSheet(u"QComboBox::drop-down{\n"
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
        self.label_2 = QLabel(self.frame)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 121, 41))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
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

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u4fdd\u7559\u5929\u6570", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u6e05\u9664\u7f13\u5b58", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
    # retranslateUi

