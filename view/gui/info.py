# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'info.ui'
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
        self.frame.setGeometry(QRect(0, 370, 800, 80))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout = QHBoxLayout(self.frame)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(10, 10, 10, 10)
        self.btnPrint = QPushButton(self.frame)
        self.btnPrint.setObjectName(u"btnPrint")
        sizePolicy = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.btnPrint.sizePolicy().hasHeightForWidth())
        self.btnPrint.setSizePolicy(sizePolicy)
        self.btnPrint.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnPrint)

        self.btnDownload = QPushButton(self.frame)
        self.btnDownload.setObjectName(u"btnDownload")
        sizePolicy.setHeightForWidth(self.btnDownload.sizePolicy().hasHeightForWidth())
        self.btnDownload.setSizePolicy(sizePolicy)
        self.btnDownload.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnDownload)

        self.btnData = QPushButton(self.frame)
        self.btnData.setObjectName(u"btnData")
        sizePolicy.setHeightForWidth(self.btnData.sizePolicy().hasHeightForWidth())
        self.btnData.setSizePolicy(sizePolicy)
        self.btnData.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnData)

        self.btnPic = QPushButton(self.frame)
        self.btnPic.setObjectName(u"btnPic")
        sizePolicy.setHeightForWidth(self.btnPic.sizePolicy().hasHeightForWidth())
        self.btnPic.setSizePolicy(sizePolicy)
        self.btnPic.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnPic)

        self.btnReport = QPushButton(self.frame)
        self.btnReport.setObjectName(u"btnReport")
        sizePolicy.setHeightForWidth(self.btnReport.sizePolicy().hasHeightForWidth())
        self.btnReport.setSizePolicy(sizePolicy)
        self.btnReport.setStyleSheet(u"QPushButton {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:#05abc2;\n"
"}\n"
"\n"
"QPushButton:pressed{\n"
"background-color: rgb(255, 0, 0);\n"
"}\n"
"")

        self.horizontalLayout.addWidget(self.btnReport)

        self.btnReturn = QPushButton(self.frame)
        self.btnReturn.setObjectName(u"btnReturn")
        sizePolicy.setHeightForWidth(self.btnReturn.sizePolicy().hasHeightForWidth())
        self.btnReturn.setSizePolicy(sizePolicy)
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

        self.horizontalLayout.addWidget(self.btnReturn)

        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 1)
        self.horizontalLayout.setStretch(2, 1)
        self.horizontalLayout.setStretch(3, 1)
        self.horizontalLayout.setStretch(4, 1)
        self.horizontalLayout.setStretch(5, 1)
        self.stackedWidget = QStackedWidget(Form)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setGeometry(QRect(0, 0, 800, 370))
        self.page = QWidget()
        self.page.setObjectName(u"page")
        self.photoLabel = QLabel(self.page)
        self.photoLabel.setObjectName(u"photoLabel")
        self.photoLabel.setGeometry(QRect(440, 0, 350, 350))
        sizePolicy1 = QSizePolicy(QSizePolicy.Fixed, QSizePolicy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.photoLabel.sizePolicy().hasHeightForWidth())
        self.photoLabel.setSizePolicy(sizePolicy1)
        self.photoLabel.setMinimumSize(QSize(350, 350))
        self.photoLabel.setMaximumSize(QSize(350, 350))
        self.photoLabel.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.photoLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.picLabel = QLabel(self.page)
        self.picLabel.setObjectName(u"picLabel")
        self.picLabel.setGeometry(QRect(10, 0, 350, 350))
        sizePolicy1.setHeightForWidth(self.picLabel.sizePolicy().hasHeightForWidth())
        self.picLabel.setSizePolicy(sizePolicy1)
        self.picLabel.setMinimumSize(QSize(350, 350))
        self.picLabel.setMaximumSize(QSize(350, 350))
        self.picLabel.setStyleSheet(u"font: 20pt \"\u5b8b\u4f53\";")
        self.picLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignTop)
        self.leftLabel = QLabel(self.page)
        self.leftLabel.setObjectName(u"leftLabel")
        self.leftLabel.setGeometry(QRect(10, 0, 350, 30))
        self.leftLabel.setStyleSheet(u"QLabel {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: transparent;\n"
"}")
        self.rightLabel = QLabel(self.page)
        self.rightLabel.setObjectName(u"rightLabel")
        self.rightLabel.setGeometry(QRect(440, 0, 350, 30))
        self.rightLabel.setStyleSheet(u"QLabel {\n"
"font: 20pt \"\u5b8b\u4f53\";\n"
"color: rgb(255, 0, 0);\n"
"background-color: transparent;\n"
"}")
        self.stackedWidget.addWidget(self.page)
        self.photoLabel.raise_()
        self.picLabel.raise_()
        self.rightLabel.raise_()
        self.leftLabel.raise_()
        self.page_2 = QWidget()
        self.page_2.setObjectName(u"page_2")
        self.tableView = QTableView(self.page_2)
        self.tableView.setObjectName(u"tableView")
        self.tableView.setGeometry(QRect(10, 0, 778, 350))
        self.tableView.setStyleSheet(u"#tableView{\n"
"	font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QComboBox {\n"
"    font: 20pt \"\u5b8b\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"	align: center;\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(0, 0, 0);/*\u80cc\u666f\u989c\u8272*/\n"
"    padding: 1px 2px 1px 2px;  /*\u9488\u5bf9\u4e8e\u7ec4\u5408\u6846\u4e2d\u7684\u6587\u672c\u5185\u5bb9*/\n"
"	color: rgb(255,255,255)\n"
"}")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QWidget()
        self.page_3.setObjectName(u"page_3")
        self.tableWidget = QTableWidget(self.page_3)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 0, 771, 370))
        self.tableWidget.setStyleSheet(u"QTableWidget{\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QTableWidget::Item\n"
"{\n"
"border:2px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QWidget()
        self.page_4.setObjectName(u"page_4")
        self.tableView_2 = QTableView(self.page_4)
        self.tableView_2.setObjectName(u"tableView_2")
        self.tableView_2.setGeometry(QRect(10, 0, 778, 370))
        self.tableView_2.setStyleSheet(u"#tableView_2{\n"
"	font: 20pt \"\u5b8b\u4f53\";\n"
"border:4px solid rgb(0,0,0);\n"
"background-color:rgb(255,255,255);\n"
"}\n"
"\n"
"QComboBox {\n"
"    font: 20pt \"\u5b8b\u4f53\";\n"
"	color: rgb(255, 255, 255);\n"
"	background-color: rgb(0,0,0);\n"
"}\n"
"\n"
"QComboBox QAbstractItemView {\n"
"	background-color: rgb(0, 0, 0);/*\u80cc\u666f\u989c\u8272*/\n"
"	color: rgb(255,255,255)\n"
"}")
        self.stackedWidget.addWidget(self.page_4)

        self.retranslateUi(Form)

        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
        self.btnPrint.setText(QCoreApplication.translate("Form", u"\u6253\u5370", None))
        self.btnDownload.setText(QCoreApplication.translate("Form", u"\u4e0b\u8f7d", None))
        self.btnData.setText(QCoreApplication.translate("Form", u"\u6570\u636e", None))
        self.btnPic.setText(QCoreApplication.translate("Form", u"\u56fe\u50cf", None))
        self.btnReport.setText(QCoreApplication.translate("Form", u"\u62a5\u544a\u5355", None))
        self.btnReturn.setText(QCoreApplication.translate("Form", u"\u8fd4\u56de", None))
        self.photoLabel.setText(QCoreApplication.translate("Form", u"test_photo", None))
        self.picLabel.setText(QCoreApplication.translate("Form", u"origin_photo", None))
        self.leftLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
        self.rightLabel.setText(QCoreApplication.translate("Form", u"TextLabel", None))
    # retranslateUi

