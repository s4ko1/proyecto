# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'BANCO.ui'
#
# Created by: PyQt5 UI code generator 5.15.9
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(677, 564)
        MainWindow.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(190, 50, 311, 151))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(270, 10, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.Movimiento = QtWidgets.QLineEdit(self.centralwidget)
        self.Movimiento.setGeometry(QtCore.QRect(110, 240, 113, 20))
        self.Movimiento.setObjectName("Movimiento")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(40, 240, 71, 16))
        self.label_2.setObjectName("label_2")
        self.monto = QtWidgets.QLineEdit(self.centralwidget)
        self.monto.setGeometry(QtCore.QRect(110, 270, 113, 20))
        self.monto.setObjectName("monto")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(60, 270, 47, 13))
        self.label_3.setObjectName("label_3")
        self.comboBox = QtWidgets.QComboBox(self.centralwidget)
        self.comboBox.setGeometry(QtCore.QRect(110, 310, 111, 22))
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(60, 310, 47, 13))
        self.label_4.setObjectName("label_4")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 350, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.pago_unico = QtWidgets.QLineEdit(self.centralwidget)
        self.pago_unico.setGeometry(QtCore.QRect(420, 240, 113, 20))
        self.pago_unico.setObjectName("pago_unico")
        self.tres_meses = QtWidgets.QLineEdit(self.centralwidget)
        self.tres_meses.setGeometry(QtCore.QRect(420, 280, 113, 20))
        self.tres_meses.setObjectName("tres_meses")
        self.seis_mese = QtWidgets.QLineEdit(self.centralwidget)
        self.seis_mese.setGeometry(QtCore.QRect(420, 320, 113, 20))
        self.seis_mese.setObjectName("seis_mese")
        self.nueve_meses = QtWidgets.QLineEdit(self.centralwidget)
        self.nueve_meses.setGeometry(QtCore.QRect(420, 360, 113, 20))
        self.nueve_meses.setObjectName("nueve_meses")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(330, 240, 81, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(330, 280, 81, 16))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(330, 320, 81, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(330, 360, 81, 16))
        self.label_8.setObjectName("label_8")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 677, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "NOMBRE"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "MONTO "))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "PLAZO"))
        self.label.setText(_translate("MainWindow", "MOVIMIENTOS"))
        self.label_2.setText(_translate("MainWindow", "MOVIMIENTO:"))
        self.label_3.setText(_translate("MainWindow", "MONTO:"))
        self.comboBox.setItemText(0, _translate("MainWindow", "PAGO ÚNICO"))
        self.comboBox.setItemText(1, _translate("MainWindow", "3 MESES"))
        self.comboBox.setItemText(2, _translate("MainWindow", "6 MESES"))
        self.comboBox.setItemText(3, _translate("MainWindow", "9 MESES"))
        self.label_4.setText(_translate("MainWindow", "PLAZOS:"))
        self.pushButton.setText(_translate("MainWindow", "AGREGAR"))
        self.label_5.setText(_translate("MainWindow", "PAGOS ÚNICOS:"))
        self.label_6.setText(_translate("MainWindow", "PAGOS 3 MESES:"))
        self.label_7.setText(_translate("MainWindow", "PAGOS 6 MESES:"))
        self.label_8.setText(_translate("MainWindow", "PAGOS 9 MESES:"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())