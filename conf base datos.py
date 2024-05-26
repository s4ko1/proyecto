import sqlite3

def create_tables():
    conn = sqlite3.connect('credit_card.db')
    c = conn.cursor()
    
    # Crear tabla de transacciones
    c.execute('''
    CREATE TABLE IF NOT EXISTS transacciones (
        id_transaccion INTEGER PRIMARY KEY AUTOINCREMENT,
        descripcion TEXT,
        monto REAL,
        fecha TEXT,
        tipo_pago TEXT,
        tasa_interes REAL,
        estado TEXT
    )
    ''')

    # Crear tabla de pagos
    c.execute('''
    CREATE TABLE IF NOT EXISTS pagos (
        id_pago INTEGER PRIMARY KEY AUTOINCREMENT,
        id_transaccion INTEGER,
        fecha_pago TEXT,
        monto_pago REAL,
        interes REAL,
        FOREIGN KEY (id_transaccion) REFERENCES transacciones (id_transaccion)
    )
    ''')

    conn.commit()
    conn.close()

create_tables()


def add_transaccion(descripcion, monto, fecha, tipo_pago, tasa_interes, estado):
    conn = sqlite3.connect('credit_card.db')
    c = conn.cursor()
    
    c.execute('''
    INSERT INTO transacciones (descripcion, monto, fecha, tipo_pago, tasa_interes, estado)
    VALUES (?, ?, ?, ?, ?, ?)
    ''', (descripcion, monto, fecha, tipo_pago, tasa_interes, estado))
    
    conn.commit()
    conn.close()

def add_pago(id_transaccion, fecha_pago, monto_pago, interes):
    conn = sqlite3.connect('credit_card.db')
    c = conn.cursor()
    
    c.execute('''
    INSERT INTO pagos (id_transaccion, fecha_pago, monto_pago, interes)
    VALUES (?, ?, ?, ?)
    ''', (id_transaccion, fecha_pago, monto_pago, interes))
    
    conn.commit()
    conn.close()


def reporte_transacciones():
    conn = sqlite3.connect('credit_card.db')
    c = conn.cursor()
    
    c.execute('''
    SELECT * FROM transacciones
    ''')
    
    transacciones = c.fetchall()
    
    for transaccion in transacciones:
        print(transaccion)
    
    conn.close()

def reporte_pagos():
    conn = sqlite3.connect('credit_card.db')
    c = conn.cursor()
    
    c.execute('''
    SELECT * FROM pagos
    ''')
    
    pagos = c.fetchall()
    
    for pago in pagos:
        print(pago)
    
    conn.close()


from datetime import datetime

def calcular_intereses():
    conn = sqlite3.connect('credit_card.db')
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

def alertas_pagos_pendientes():
    conn = sqlite3.connect('credit_card.db')
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


def main():
    while True:
        print("1. Añadir transacción")
        print("2. Añadir pago")
        print("3. Ver reporte de transacciones")
        print("4. Ver reporte de pagos")
        print("5. Calcular intereses")
        print("6. Ver alertas de pagos pendientes")
        print("7. Salir")
        
        opcion = input("Selecciona una opción: ")
        
        if opcion == '1':
            descripcion = input("Descripción: ")
            monto = float(input("Monto: "))
            fecha = input("Fecha (YYYY-MM-DD): ")
            tipo_pago = input("Tipo de pago (pago único, 3 meses, 9 meses): ")
            tasa_interes = float(input("Tasa de interés (%): "))
            estado = input("Estado (pendiente, pagado): ")
            add_transaccion(descripcion, monto, fecha, tipo_pago, tasa_interes, estado)
        elif opcion == '2':
            id_transaccion = int(input("ID de la transacción: "))
            fecha_pago = input("Fecha de pago (YYYY-MM-DD): ")
            monto_pago = float(input("Monto del pago: "))
            interes = float(input("Interés: "))
            add_pago(id_transaccion, fecha_pago, monto_pago, interes)
        elif opcion == '3':
            reporte_transacciones()
        elif opcion == '4':
            reporte_pagos()
        elif opcion == '5':
            calcular_intereses()
        elif opcion == '6':
            alertas_pagos_pendientes()
        elif opcion == '7':
            break
        else:
            print("Opción no válida. Inténtalo de nuevo.")

if __name__ == '__main__':
    main()

