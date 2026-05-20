import pandas as pd
import mysql.connector

# Leer CSV
df = pd.read_csv("tablas/empleados.csv", sep=";")

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
INSERT INTO empleados (
    id_empleado,
    nombre_empleado
)
VALUES (%s, %s)
"""

datos = [tuple(x) for x in df.to_numpy()]

cursor.executemany(sql, datos)

conexion.commit()

print(f"{cursor.rowcount} empleados insertados.")

cursor.close()
conexion.close()