import pandas as pd
import mysql.connector

# Leer CSV
df = pd.read_csv("tablas/metodos_pago.csv", sep=";")

# Conexión MySQL
conexion = mysql.connector.connect(
    host="localhost",
    user="root",
    password="root",
    database="mi_base_datos"
)

cursor = conexion.cursor()

# Insertar datos
sql = """
INSERT INTO metodos_pago (
    id_metodo_pago,
    metodo_pago
)
VALUES (%s, %s)
"""

datos = [tuple(x) for x in df.to_numpy()]

cursor.executemany(sql, datos)

conexion.commit()

print(f"{cursor.rowcount} métodos de pago insertados.")

cursor.close()
conexion.close()