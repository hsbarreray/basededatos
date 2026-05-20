import pandas as pd
import mysql.connector

# Leer CSV
df = pd.read_csv("tablas/pedidos.csv", sep=";")

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
INSERT INTO pedidos (
    id_pedido,
    hora,
    tiempo_atencion,
    error_pedido,
    num_clientes_en_cola,
    id_producto,
    id_metodo_pago,
    id_empleado
)
VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
"""

datos = [tuple(x) for x in df.to_numpy()]

cursor.executemany(sql, datos)

conexion.commit()

print(f"{cursor.rowcount} pedidos insertados.")

cursor.close()
conexion.close()