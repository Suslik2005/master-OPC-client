# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'new_value.ui'
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
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QFrame,
    QHBoxLayout, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(530, 301)
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
        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.comboBox_UZEL = QComboBox(self.frame)
        self.comboBox_UZEL.setObjectName(u"comboBox_UZEL")
        self.comboBox_UZEL.setTabletTracking(False)
        self.comboBox_UZEL.setStyleSheet(u"color: white;\n"
"padding-left: 10px;\n"
"font-size: 12pt;\n"
"\n"
"")

        self.horizontalLayout_2.addWidget(self.comboBox_UZEL)

        self.pushButton_UZEL = QPushButton(self.frame)
        self.pushButton_UZEL.setObjectName(u"pushButton_UZEL")
        self.pushButton_UZEL.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-size: 8pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 25px;\n"
"height: 25 px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_2.addWidget(self.pushButton_UZEL)


        self.verticalLayout.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.comboBox_USTRO = QComboBox(self.frame)
        self.comboBox_USTRO.setObjectName(u"comboBox_USTRO")
        self.comboBox_USTRO.setStyleSheet(u"color: white;\n"
"padding-left: 10px;\n"
"font-size: 12pt;\n"
"\n"
"")

        self.horizontalLayout_3.addWidget(self.comboBox_USTRO)

        self.pushButton_format = QPushButton(self.frame)
        self.pushButton_format.setObjectName(u"pushButton_format")
        self.pushButton_format.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"font-size: 8pt;\n"
"background-color: rgba(255,255,255,30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;\n"
"width: 25px;\n"
"height: 25 px;\n"
"}\n"
"QPushButton:hover {\n"
"background-color: rgba(255,255,255,30);\n"
"}\n"
"QPushButton:pressed{\n"
"background-color: rgba(255,255,255,70);\n"
"}")

        self.horizontalLayout_3.addWidget(self.pushButton_format)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.comboBox_values = QComboBox(self.frame)
        self.comboBox_values.setObjectName(u"comboBox_values")
        self.comboBox_values.setStyleSheet(u"color: white;\n"
"padding-left: 10px;\n"
"font-size: 12pt;\n"
"\n"
"")

        self.verticalLayout.addWidget(self.comboBox_values)

        self.lineEdit_value = QLineEdit(self.frame)
        self.lineEdit_value.setObjectName(u"lineEdit_value")
        self.lineEdit_value.setStyleSheet(u"font-size: 12pt;\n"
"color: white;\n"
"padding-left: 10px;\n"
"")

        self.verticalLayout.addWidget(self.lineEdit_value)

        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.pushButton_valueadd = QPushButton(self.frame)
        self.pushButton_valueadd.setObjectName(u"pushButton_valueadd")
        self.pushButton_valueadd.setStyleSheet(u"QPushButton{\n"
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

        self.horizontalLayout.addWidget(self.pushButton_valueadd)


        self.verticalLayout.addLayout(self.horizontalLayout)


        self.verticalLayout_2.addWidget(self.frame)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.comboBox_UZEL.setCurrentText("")
        self.pushButton_UZEL.setText(QCoreApplication.translate("Dialog", u"apply", None))
        self.pushButton_format.setText(QCoreApplication.translate("Dialog", u"apply", None))
        self.lineEdit_value.setPlaceholderText(QCoreApplication.translate("Dialog", u"value", None))
        self.pushButton_valueadd.setText(QCoreApplication.translate("Dialog", u"\u0414\u043e\u0431\u0430\u0432\u0438\u0442\u044c", None))
    # retranslateUi

