import sys
from PyQt5 import QtWidgets, uic
import sqlite3
from datetime import datetime

class CreditCardManager(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('credit_card_manager.ui', self)

        # Conectar botones a funciones
        self.btnAddTransaction.clicked.connect(self.add_transaction)
        self.btnAddPayment.clicked.connect(self.add_payment)
        self.btnGenerateReportTransactions.clicked.connect(self.reporte_transacciones)
        self.btnGenerateReportPayments.clicked.connect(self.reporte_pagos)
        self.btnShowAlerts.clicked.connect(self.alertas_pagos_pendientes)

        # Cargar datos iniciales
        self.load_transactions()
        self.load_payments()

    def create_connection(self):
        return sqlite3.connect('credit_card.db')

    def load_transactions(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM transacciones')
        transactions = c.fetchall()
        self.tblTransactions.setRowCount(0)
        for row_number, row_data in enumerate(transactions):
            self.tblTransactions.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tblTransactions.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def load_payments(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM pagos')
        payments = c.fetchall()
        self.tblPayments.setRowCount(0)
        for row_number, row_data in enumerate(payments):
            self.tblPayments.insertRow(row_number)
            for column_number, data in enumerate(row_data):
                self.tblPayments.setItem(row_number, column_number, QtWidgets.QTableWidgetItem(str(data)))
        conn.close()

    def add_transaction(self):
        descripcion = self.txtDescription.text()
        monto = float(self.txtAmount.text())
        fecha = self.txtDate.text()
        tipo_pago = self.cmbPaymentType.currentText()
        tasa_interes = float(self.txtInterestRate.text())
        estado = self.cmbStatus.currentText()

        conn = self.create_connection()
        c = conn.cursor()
        c.execute('''
        INSERT INTO transacciones (descripcion, monto, fecha, tipo_pago, tasa_interes, estado)
        VALUES (?, ?, ?, ?, ?, ?)
        ''', (descripcion, monto, fecha, tipo_pago, tasa_interes, estado))
        conn.commit()
        conn.close()
        self.load_transactions()

    def add_payment(self):
        id_transaccion = int(self.txtTransactionID.text())
        fecha_pago = self.txtPaymentDate.text()
        monto_pago = float(self.txtPaymentAmount.text())
        interes = float(self.txtInterest.text())

        conn = self.create_connection()
        c = conn.cursor()
        c.execute('''
        INSERT INTO pagos (id_transaccion, fecha_pago, monto_pago, interes)
        VALUES (?, ?, ?, ?)
        ''', (id_transaccion, fecha_pago, monto_pago, interes))
        conn.commit()
        conn.close()
        self.load_payments()

    def reporte_transacciones(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM transacciones')
        transactions = c.fetchall()
        for transaccion in transactions:
            print(transaccion)
        conn.close()

    def reporte_pagos(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('SELECT * FROM pagos')
        payments = c.fetchall()
        for pago in payments:
            print(pago)
        conn.close()

    def calcular_intereses(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('''
        SELECT id_transaccion, monto, tasa_interes, tipo_pago, fecha, estado FROM transacciones
        WHERE estado = 'pendiente'
        ''')
        transacciones = c.fetchall()
        for transaccion in transacciones:
            id_transaccion, monto, tasa_interes, tipo_pago, fecha, estado = transaccion
            if tipo_pago != 'pago único':
                meses = int(tipo_pago.split()[0])
                fecha_inicio = datetime.strptime(fecha, '%Y-%m-%d')
                fecha_actual = datetime.now()
                meses_transcurridos = (fecha_actual.year - fecha_inicio.year) * 12 + fecha_actual.month - fecha_inicio.month
                if meses_transcurridos > 0:
                    interes_acumulado = monto * (tasa_interes / 100) * meses_transcurridos
                    print(f'Transacción {id_transaccion} tiene un interés acumulado de: {interes_acumulado:.2f}')
        conn.close()

    def alertas_pagos_pendientes(self):
        conn = self.create_connection()
        c = conn.cursor()
        c.execute('''
        SELECT id_transaccion, descripcion, monto, fecha FROM transacciones
        WHERE estado = 'pendiente'
        ''')
        transacciones_pendientes = c.fetchall()
        for transaccion in transacciones_pendientes:
            id_transaccion, descripcion, monto, fecha = transaccion
            print(f'Alerta: Transacción {id_transaccion} - {descripcion} de {monto} está pendiente desde {fecha}')
        conn.close()

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = CreditCardManager()
    mainWindow.show()
    sys.exit(app.exec_())
