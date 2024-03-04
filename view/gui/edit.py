# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'edit.ui'
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
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 350))
        self.stackedWidget.setStyleSheet(u"")
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.delete_icon_label = QLabel(self.page)
        self.delete_icon_label.setObjectName(u"delete_icon_label")
        self.delete_icon_label.setGeometry(QRect(310, 240, 80, 80))
        self.delete_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.btnAdd = QPushButton(self.page)
        self.btnAdd.setObjectName(u"btnAdd")
        self.btnAdd.setGeometry(QRect(310, 40, 280, 80))
        self.btnAdd.setStyleSheet(u"QPushButton {\n"
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
        self.btnModify = QPushButton(self.page)
        self.btnModify.setObjectName(u"btnModify")
        self.btnModify.setGeometry(QRect(310, 140, 280, 80))
        self.btnModify.setStyleSheet(u"QPushButton {\n"
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
        self.label = QLabel(self.page)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 0, 121, 51))
        self.label.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.add_icon_label = QLabel(self.page)
        self.add_icon_label.setObjectName(u"add_icon_label")
        self.add_icon_label.setGeometry(QRect(310, 40, 80, 80))
        self.add_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.btnDelete = QPushButton(self.page)
        self.btnDelete.setObjectName(u"btnDelete")
        self.btnDelete.setGeometry(QRect(310, 240, 280, 80))
        self.btnDelete.setStyleSheet(u"QPushButton {\n"
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
        self.edit_icon_label = QLabel(self.page)
        self.edit_icon_label.setObjectName(u"edit_icon_label")
        self.edit_icon_label.setGeometry(QRect(310, 140, 80, 80))
        self.edit_icon_label.setStyleSheet(u"font: 20pt \"\u5e7c\u5706\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color: rgb(255, 255, 255);\n"
"border-radius: 35px;\n"
"\n"
"")
        self.stackedWidget.addWidget(self.page)
        self.btnAdd.raise_()
        self.btnModify.raise_()
        self.label.raise_()
        self.add_icon_label.raise_()
        self.btnDelete.raise_()
        self.edit_icon_label.raise_()
        self.delete_icon_label.raise_()
        self.page2 = QWidget()
        self.page2.setObjectName(u"page2")
        self.label_5 = QLabel(self.page2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(0, 0, 378, 27))
        self.label_5.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_3 = QLabel(self.page2)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(190, 200, 151, 44))
        self.label_3.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.nameLine = QLineEdit(self.page2)
        self.nameLine.setObjectName(u"nameLine")
        self.nameLine.setGeometry(QRect(390, 90, 230, 70))
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.nameLine.sizePolicy().hasHeightForWidth())
        self.nameLine.setSizePolicy(sizePolicy)
        self.nameLine.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 255, 255);\n"
"background-color: rgb(0, 0, 0);")
        self.rowCb = QComboBox(self.page2)
        self.rowCb.setObjectName(u"rowCb")
        self.rowCb.setGeometry(QRect(390, 190, 230, 70))
        self.rowCb.setStyleSheet(u"QComboBox::drop-down{\n"
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
        self.label_2 = QLabel(self.page2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(130, 100, 211, 44))
        self.label_2.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.stackedWidget.addWidget(self.page2)
        self.page3 = QWidget()
        self.page3.setObjectName(u"page3")
        self.label_6 = QLabel(self.page3)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, 0, 161, 47))
        self.label_6.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.deleteCb = QComboBox(self.page3)
        self.deleteCb.setObjectName(u"deleteCb")
        self.deleteCb.setGeometry(QRect(380, 140, 230, 70))
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.deleteCb.sizePolicy().hasHeightForWidth())
        self.deleteCb.setSizePolicy(sizePolicy1)
        self.deleteCb.setStyleSheet(u"QComboBox::drop-down{\n"
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
        self.label_7 = QLabel(self.page3)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(140, 140, 181, 71))
        self.label_7.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.stackedWidget.addWidget(self.page3)
        self.page4 = QWidget()
        self.page4.setObjectName(u"page4")
        self.editCb = QComboBox(self.page4)
        self.editCb.setObjectName(u"editCb")
        self.editCb.setGeometry(QRect(380, 140, 230, 70))
        sizePolicy1.setHeightForWidth(self.editCb.sizePolicy().hasHeightForWidth())
        self.editCb.setSizePolicy(sizePolicy1)
        self.editCb.setStyleSheet(u"QComboBox::drop-down{\n"
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
        self.label_9 = QLabel(self.page4)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(140, 140, 180, 70))
        self.label_9.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.label_8 = QLabel(self.page4)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(0, 0, 161, 47))
        self.label_8.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.stackedWidget.addWidget(self.page4)
        self.page5 = QWidget()
        self.page5.setObjectName(u"page5")
        self.reagentTable = QTableView(self.page5)
        self.reagentTable.setObjectName(u"reagentTable")
        self.reagentTable.setGeometry(QRect(10, 10, 781, 334))
        self.reagentTable.setStyleSheet(u"#reagentTable\n"
"{	\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QComboBox {\n"
"   font: 20pt \"\u5b8b\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0, 0, 0);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(0, 0, 0);/*\u80cc\u666f\u989c\u8272*/\n"
"    padding: 1px 2px 1px 2px;  /*\u9488\u5bf9\u4e8e\u7ec4\u5408\u6846\u4e2d\u7684\u6587\u672c\u5185\u5bb9*/\n"
"	color: rgb(255,255,255)\n"
"}")
        self.stackedWidget.addWidget(self.page5)
        self.frame = QFrame(Form)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 350, 800, 100))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.btnConfirm = QPushButton(self.frame)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setGeometry(QRect(10, 10, 380, 80))
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
        self.btnReturn.setGeometry(QRect(410, 10, 380, 80))
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

        self.stackedWidget.setCurrentIndex(4)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.delete_icon_label.setText("")
        self.btnAdd.setText(QCoreApplication.translate("Form", u"    \u6dfb\u52a0\u8bd5\u5242\u5361", None))
        self.btnModify.setText(QCoreApplication.translate("Form", u"    \u4fee\u6539\u8bd5\u5242\u5361", None))
        self.label.setText(QCoreApplication.translate("Form", u"\u68c0\u75ab\u8bbe\u7f6e", None))
        self.add_icon_label.setText("")
        self.btnDelete.setText(QCoreApplication.translate("Form", u"   \u5220\u9664\u8bd5\u5242\u5361", None))
        self.edit_icon_label.setText("")
        self.label_5.setText(QCoreApplication.translate("Form", u"\u6dfb\u52a0\u8bd5\u5242\u5361", None))
        self.label_3.setText(QCoreApplication.translate("Form", u"\u89c4\u683c", None))
        self.label_2.setText(QCoreApplication.translate("Form", u"\u8bd5\u5242\u5361\u578b\u53f7", None))
        self.label_6.setText(QCoreApplication.translate("Form", u"\u5220\u9664\u8bd5\u5242\u5361", None))
        self.label_7.setText(QCoreApplication.translate("Form", u"\u8bd5\u5242\u5361\u578b\u53f7", None))
        self.label_9.setText(QCoreApplication.translate("Form", u"\u8bd5\u5242\u5361\u578b\u53f7", None))
        self.label_8.setText(QCoreApplication.translate("Form", u"\u4fee\u6539\u8bd5\u5242\u5361", None))
        self.btnConfirm.setText(QCoreApplication.translate("Form", u"\u786e\u8ba4", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
    # retranslateUi

