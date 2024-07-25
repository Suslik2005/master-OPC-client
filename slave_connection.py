# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'slave_connection.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QLineEdit,
    QPushButton, QSizePolicy, QVBoxLayout, QWidget)

class Ui_Dialog1(object):
    def setupUi(self, Dialog1):
        if not Dialog1.objectName():
            Dialog1.setObjectName(u"Dialog1")
        Dialog1.resize(361, 143)
        Dialog1.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog1)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog1)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"backgorund-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"font-size: 12pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout_3.addWidget(self.lineEdit)

        self.pushButton_connection = QPushButton(self.frame)
        self.pushButton_connection.setObjectName(u"pushButton_connection")
        self.pushButton_connection.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-size: 12pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 230px;\n"
"height: 50 px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.verticalLayout_3.addWidget(self.pushButton_connection)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog1)

        QMetaObject.connectSlotsByName(Dialog1)
    # setupUi

    def retranslateUi(self, Dialog1):
        Dialog1.setWindowTitle(QCoreApplication.translate("Dialog1", u"Dialog", None))
        self.lineEdit.setText(QCoreApplication.translate("Dialog1", u"54000", None))
        self.lineEdit.setPlaceholderText(QCoreApplication.translate("Dialog1", u"localhost", None))
        self.pushButton_connection.setText(QCoreApplication.translate("Dialog1", u"\u041f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
    # retranslateUi

