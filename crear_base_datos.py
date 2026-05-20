import mysql.connector

host = "localhost"
user = "root"
password = "root"
database_name = "mi_base_datos"

# Conexión al servidor MySQL
conn = mysql.connector.connect(
    host=host,
    user=user,
    password=password
)

cursor = conn.cursor()

# Crear base de datos
cursor.execute(f"CREATE DATABASE IF NOT EXISTS {database_name}")

print(f"Base de datos '{database_name}' creada correctamente.")

# Usar base de datos
conn.database = database_name

# TABLA PRODUCTOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id_producto INT PRIMARY KEY,
    tipo_producto VARCHAR(100)
)
""")

# TABLA METODOS_PAGO
cursor.execute("""
CREATE TABLE IF NOT EXISTS metodos_pago (
    id_metodo_pago INT PRIMARY KEY,
    metodo_pago VARCHAR(100)
)
""")

# TABLA EMPLEADOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS empleados (
    id_empleado INT PRIMARY KEY,
    nombre_empleado VARCHAR(100)
)
""")

# TABLA PEDIDOS
cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos (
    id_pedido INT PRIMARY KEY,
    hora TIME,
    tiempo_atencion INT,
    error_pedido VARCHAR(50),
    num_clientes_en_cola INT,

    id_producto INT,
    id_metodo_pago INT,
    id_empleado INT,

    FOREIGN KEY (id_producto)
        REFERENCES productos(id_producto),

    FOREIGN KEY (id_metodo_pago)
        REFERENCES metodos_pago(id_metodo_pago),

    FOREIGN KEY (id_empleado)
        REFERENCES empleados(id_empleado)
)
""")

conn.commit()

print("Tablas creadas correctamente.")

cursor.close()
conn.close()