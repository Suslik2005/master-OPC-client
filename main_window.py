# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHBoxLayout,
    QHeaderView, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1047, 377)
        MainWindow.setMinimumSize(QSize(819, 0))
        MainWindow.setStyleSheet(u"background-color: qlineargradient(spread:pad, x1:1, y1:1, x2:0, y2:0, stop:0 rgba(81, 0, 135, 255), stop:0.427447 rgba(41, 61, 132, 235), stop:1 rgba(155, 79, 165, 255));\n"
"font-family: Noto Sans SC;")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_3 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.balance_frame = QFrame(self.centralwidget)
        self.balance_frame.setObjectName(u"balance_frame")
        self.balance_frame.setStyleSheet(u"background-color: rgba(255,255,255, 30);\n"
"border: 1px solid rgba(255,255,255,40);\n"
"border-radius: 7px;")
        self.verticalLayout_2 = QVBoxLayout(self.balance_frame)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.pushButton_disconnect = QPushButton(self.balance_frame)
        self.pushButton_disconnect.setObjectName(u"pushButton_disconnect")
        self.pushButton_disconnect.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
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
        icon = QIcon()
        icon.addFile(u"../DesignProject/icons/cancel_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_disconnect.setIcon(icon)

        self.horizontalLayout_3.addWidget(self.pushButton_disconnect)

        self.pushButton_connect = QPushButton(self.balance_frame)
        self.pushButton_connect.setObjectName(u"pushButton_connect")
        self.pushButton_connect.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
"background-color: rgba(255,0,0,30);\n"
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
        icon1 = QIcon()
        icon1.addFile(u"../DesignProject/icons/wifi_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_connect.setIcon(icon1)

        self.horizontalLayout_3.addWidget(self.pushButton_connect)

        self.pushButton_add = QPushButton(self.balance_frame)
        self.pushButton_add.setObjectName(u"pushButton_add")
        self.pushButton_add.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
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
        icon2 = QIcon()
        icon2.addFile(u"../DesignProject/icons/add_circle_24dp_FILL0_wght400_GRAD0_opsz24.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_add.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.pushButton_add)

        self.pushButton_add_2 = QPushButton(self.balance_frame)
        self.pushButton_add_2.setObjectName(u"pushButton_add_2")
        self.pushButton_add_2.setStyleSheet(u"QPushButton{\n"
"color: white;\n"
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
        self.pushButton_add_2.setIcon(icon2)

        self.horizontalLayout_3.addWidget(self.pushButton_add_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")

        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.tableWidget_zapis = QTableWidget(self.balance_frame)
        if (self.tableWidget_zapis.columnCount() < 3):
            self.tableWidget_zapis.setColumnCount(3)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget_zapis.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget_zapis.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget_zapis.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        self.tableWidget_zapis.setObjectName(u"tableWidget_zapis")
        self.tableWidget_zapis.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_zapis.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_zapis.setTabKeyNavigation(False)
        self.tableWidget_zapis.setProperty("showDropIndicator", False)

        self.horizontalLayout_2.addWidget(self.tableWidget_zapis)

        self.tableWidget_2 = QTableWidget(self.balance_frame)
        if (self.tableWidget_2.columnCount() < 3):
            self.tableWidget_2.setColumnCount(3)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem5)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.tableWidget_2.setTabKeyNavigation(False)
        self.tableWidget_2.setProperty("showDropIndicator", False)

        self.horizontalLayout_2.addWidget(self.tableWidget_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.verticalLayout_2.addLayout(self.verticalLayout_4)


        self.verticalLayout_3.addWidget(self.balance_frame)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"modbus", None))
        self.pushButton_disconnect.setText(QCoreApplication.translate("MainWindow", u"\u043e\u0442\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.pushButton_connect.setText(QCoreApplication.translate("MainWindow", u"\u043f\u043e\u0434\u043a\u043b\u044e\u0447\u0438\u0442\u044c\u0441\u044f", None))
        self.pushButton_add.setText(QCoreApplication.translate("MainWindow", u"\u0437\u0430\u0434\u0430\u0442\u044c \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        self.pushButton_add_2.setText(QCoreApplication.translate("MainWindow", u"\u0432\u044b\u0432\u0435\u0441\u0442\u0438 \u0437\u043d\u0430\u0447\u0435\u043d\u0438\u0435", None))
        ___qtablewidgetitem = self.tableWidget_zapis.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem1 = self.tableWidget_zapis.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"value", None));
        ___qtablewidgetitem2 = self.tableWidget_zapis.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"type", None));
        ___qtablewidgetitem3 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"name", None));
        ___qtablewidgetitem4 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"value", None));
        ___qtablewidgetitem5 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"type", None));
    # retranslateUi

