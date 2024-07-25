import sys

import threading
import PySide6
from PySide6 import QtWidgets, QtGui
from PySide6.QtWidgets import QApplication, QMainWindow
from opcua import Client

from main_window import Ui_MainWindow
from new_value import Ui_Dialog
from slave_connection import Ui_Dialog1
from print_value import Ui_Dialog3


class Slave(QMainWindow):
    def __init__(self):
        super(Slave, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.connected = False
        self.bruh = None
        self.uzel = None
        self.device = None
        self.ustro = None
        self.client = None
        self.counter = 0
        self.uchet_dict = {}
        self.dict = {}
        self.revizor_dict = {}
        self.ui.tableWidget_zapis.setColumnCount(3)

        self.ui.pushButton_add.clicked.connect(self.open_new_value)
        self.ui.pushButton_add_2.clicked.connect(self.open_new_print_value)
        self.ui.pushButton_connect.clicked.connect(self.connec)

        self.ui.pushButton_disconnect.clicked.connect(self.disc)

    def connec(self):
        self.new_window = QtWidgets.QDialog()
        self.ui_window = Ui_Dialog1()
        self.ui_window.setupUi(self.new_window)
        self.new_window.show()
        self.ui_window.pushButton_connection.clicked.connect(self.super_connect)

    def disc(self):
        self.client.disconnect()
        print(1)
        self.connected = False
        button = self.ui.pushButton_connect
        button.setStyleSheet(
            'QPushButton {background-color: rgba(255,0,0,30);width: 230px; height: 50 px; color: white;}')
        print(3)
    def super_connect(self):
        localehost = self.ui_window.lineEdit.text()
        self.client = Client("opc.tcp://localhost:{}/freeopcua/server/".format(localehost))
        button = self.ui.pushButton_connect
        try:
            self.client.connect()
            print(1)
            self.client.load_type_definitions()
            print(2)
            button.setStyleSheet(
                'QPushButton {background-color: rgba(0,255,0,30);width: 230px; height: 50 px; color: white;}')
            self.connected = True
            print(3)
        except:
            pass
        self.new_window.close()

    def potok1(self, a):
        for i in range(3):
            b = PySide6.QtWidgets.QTableWidgetItem(str(a[i + 1]))
            self.ui.tableWidget_2.setItem(self.counter - 1, i, b)
        t1 = threading.Thread(target=self.revizor_vivod, args=(), daemon=True)
        t1.start()

    def open_new_print_value(self):
        self.new_window2 = QtWidgets.QDialog()
        self.print_value = Ui_Dialog3()
        self.print_value.setupUi(self.new_window2)
        self.new_window2.show()
        self.print_value.pushButton_valueprint.clicked.connect(self.vivod)

    def revizor_vivod(self):
        while True:
            print(self.revizor_dict)
            for i in self.revizor_dict.items():
                print(self.revizor_dict[i])
                self.ui.tableWidget_2.item(i).setText(str(v[2]))

    def vivod(self):
        name2 = self.print_value.lineEdit_value_name.text()
        name = self.uzel
        name1 = self.device

        if name2 in self.dict:
            var = self.client.get_node(f'ns=1;s={name}.{name1}.{name2}')
            c = var.get_data_value()
            format = str(c).split(':')[3].split(')')[0]
            value = str(c).split(':')[2].split(',')[0]
            self.revizor_dict[name2] = [value, format]
            self.counter += 1
            self.ui.tableWidget_2.setRowCount(self.counter)
            self.potok1(self.revizor_dict[name2])
            self.new_window1.close()

    def button1(self):
        self.uzel = self.new_value.comboBox_UZEL.currentText()
        list = [self.tr(i) for i in self.uchet_dict[self.uzel]]
        self.new_value.comboBox_USTRO.addItems(list)
        print(list)

    def format_returner(self, format):
        if format == "float32":
            a = 'VariantType.Float'
        elif format == "int32":
            a = 'VariantType.Int32'
        elif format == 'uint32':
            a = 'VariantType.UInt32'
        elif format == "double64":
            a = 'VariantType.Double'
        print(a)
        return a

    def button2(self):
        self.new_value.comboBox_3.clear()
        self.ustro = self.new_value.comboBox_USTRO.currentText()
        format = self.new_value.comboBox_formats.currentText()
        b = self.format_returner(format)
        list = [self.tr(i[0]) for i in self.uchet_dict[self.uzel][self.ustro].items() if b == i[1]]
        print(list)
        self.new_value.comboBox_3.addItems(list)

    def open_new_value(self):
        self.new_window1 = QtWidgets.QDialog()
        self.new_value = Ui_Dialog()
        self.new_value.setupUi(self.new_window1)
        self.new_window1.show()

        if self.uzel == None:
            objects = self.client.get_objects_node()
            o = objects.get_children()[1]
            for i in o.get_children():
                a = str(i.get_browse_name())
                name = a[a.find(":") + 1:a.find(")")]
                self.uchet_dict[name] = {}
                for i1 in i.get_children():
                    a1 = str(i1.get_browse_name())
                    name1 = a1[a1.find(":") + 1:a1.rfind(")")]
                    self.uchet_dict[name][name1] = {}
                    for i2 in i1.get_children():
                        a2 = str(i2.get_browse_name())
                        name2 = a2[a2.find(":") + 1:a2.rfind(")")]
                        var = self.client.get_node(f'ns=1;s={name}.{name1}.{name2}')
                        print(var)
                        var.set_value(0)
                        c = var.get_data_value()
                        format = str(c).split(':')[3].split(')')[0]
                        self.uchet_dict[name][name1][name2] = format
            list = [self.tr(i) for i in self.uchet_dict]
            print(self.uchet_dict)
            self.new_value.comboBox_UZEL.addItems(list)
            print('ok')
        else:
            list = [self.tr(i) for i in self.uchet_dict]
            print(list)
            self.new_value.comboBox_UZEL.addItems(list)

        self.new_value.pushButton_UZEL.clicked.connect(self.button1)
        self.new_value.pushButton_format.clicked.connect(self.button2)
        self.new_value.pushButton_valueadd.clicked.connect(self.add_new_value)

    def add_new_value(self):
        self.uzel = self.new_value.comboBox_UZEL.currentText()
        if self.device == None:
            self.device = self.new_value.comboBox_USTRO.currentText()
        vaalue = self.new_value.lineEdit_value.text()
        name = self.uzel
        name1 = self.device
        name2 = self.new_value.comboBox_3.currentText()
        var = self.client.get_node(f'ns=1;s={name}.{name1}.{name2}')
        print(var)
        var.set_value(vaalue)
        format = self.new_value.comboBox_formats.currentText()
        a = [name2, vaalue, format]
        self.dict[name2] = [vaalue, format]
        self.ui.tableWidget_zapis.setRowCount(len(self.dict))
        print(self.dict)
        for i in range(3):
            b = PySide6.QtWidgets.QTableWidgetItem(str(a[i]))
            self.ui.tableWidget_zapis.setItem(len(self.dict) - 1, i, b)
        self.new_window1.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Slave()
    window.show()
    sys.exit(app.exec())
