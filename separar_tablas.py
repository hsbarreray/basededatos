import pandas as pd
import os

# Leer Excel
df = pd.read_excel("datos/datos_calidad.xlsx")

# Crear carpeta tablas si no existe
os.makedirs("tablas", exist_ok=True)

# =========================
# TABLA PRODUCTOS
# =========================
productos = df[["tipo_producto"]].drop_duplicates().reset_index(drop=True)

productos["id_producto"] = productos.index + 1

productos = productos[["id_producto", "tipo_producto"]]

# =========================
# TABLA METODOS_PAGO
# =========================
metodos_pago = df[["metodo_pago"]].drop_duplicates().reset_index(drop=True)

metodos_pago["id_metodo_pago"] = metodos_pago.index + 1

metodos_pago = metodos_pago[["id_metodo_pago", "metodo_pago"]]

# =========================
# TABLA EMPLEADOS
# =========================
empleados = df[["empleado"]].drop_duplicates().reset_index(drop=True)

empleados["id_empleado"] = empleados.index + 1

empleados = empleados.rename(columns={
    "empleado": "nombre_empleado"
})

empleados = empleados[["id_empleado", "nombre_empleado"]]

# =========================
# RELACIONES PARA PEDIDOS
# =========================

df = df.merge(
    productos,
    on="tipo_producto",
    how="left"
)

df = df.merge(
    metodos_pago,
    on="metodo_pago",
    how="left"
)

df = df.merge(
    empleados,
    left_on="empleado",
    right_on="nombre_empleado",
    how="left"
)

# =========================
# TABLA PEDIDOS
# =========================

pedidos = pd.DataFrame()

pedidos["id_pedido"] = df["id_pedido"]
pedidos["hora"] = df["hora"]
pedidos["tiempo_atencion"] = df["tiempo_atencion"]
pedidos["error_pedido"] = df["error_pedido"]
pedidos["num_clientes_en_cola"] = df["num_clientes_en_cola"]

pedidos["id_producto"] = df["id_producto"]
pedidos["id_metodo_pago"] = df["id_metodo_pago"]
pedidos["id_empleado"] = df["id_empleado"]

# =========================
# GUARDAR CSV
# =========================

productos.to_csv(
    "tablas/productos.csv",
    index=False,
    sep=";"
)

metodos_pago.to_csv(
    "tablas/metodos_pago.csv",
    index=False,
    sep=";"
)

empleados.to_csv(
    "tablas/empleados.csv",
    index=False,
    sep=";"
)

pedidos.to_csv(
    "tablas/pedidos.csv",
    index=False,
    sep=";"
)

print("Tablas separadas correctamente.")