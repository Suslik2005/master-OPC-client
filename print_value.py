# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'print_value.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QFrame, QHBoxLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog3(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(538, 166)
        Dialog.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;\n"
"")
        self.verticalLayout_2 = QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.frame = QFrame(Dialog)
        self.frame.setObjectName(u"frame")
        self.frame.setStyleSheet(u"backgorund-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"")
        self.frame.setFrameShape(QFrame.NoFrame)
        self.verticalLayout = QVBoxLayout(self.frame)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.is_all_ok = QLabel(self.frame)
        self.is_all_ok.setObjectName(u"is_all_ok")
        self.is_all_ok.setStyleSheet(u"color: white;\n"
"font-size: 12pt;\n"
"background-color: green;\n"
"border: none;")

        self.verticalLayout.addWidget(self.is_all_ok)

        self.lineEdit_value_name = QLineEdit(self.frame)
        self.lineEdit_value_name.setObjectName(u"lineEdit_value_name")
        self.lineEdit_value_name.setStyleSheet(u"font-size: 12pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.lineEdit_value_name)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_valueprint = QPushButton(self.frame)
        self.pushButton_valueprint.setObjectName(u"pushButton_valueprint")
        self.pushButton_valueprint.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.pushButton_valueprint)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.is_all_ok.setText(QCoreApplication.translate("Dialog", u"All is ok", None))
        self.lineEdit_value_name.setPlaceholderText(QCoreApplication.translate("Dialog", u"value name", None))
        self.pushButton_valueprint.setText(QCoreApplication.translate("Dialog", u"\u0412\u044b\u0432\u0435\u0441\u0442\u0438", None))
    # retranslateUi

