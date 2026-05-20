import mysql.connector
from mysql.connector import Error
import datetime

def consultar_tablas():

    conexion = None

    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="mi_base_datos"
        )

        if conexion.is_connected():

            print("Conexión exitosa a MySQL")

            cursor = conexion.cursor()

            tablas = [
                "productos",
                "metodos_pago",
                "empleados",
                "pedidos"
            ]

            for tabla in tablas:

                print("\n" + "=" * 50)
                print(f"TABLA: {tabla.upper()}")
                print("=" * 50)

                cursor.execute(f"SELECT * FROM {tabla}")

                resultados = cursor.fetchall()

                # Mostrar nombres de columnas
                columnas = [i[0] for i in cursor.description]
                print(columnas)

                # Mostrar registros
                for fila in resultados:

                    fila_limpia = []

                    for dato in fila:

                        # Convertir TIME a formato legible
                        if isinstance(dato, datetime.timedelta):

                            total_segundos = int(dato.total_seconds())

                            horas = total_segundos // 3600
                            minutos = (total_segundos % 3600) // 60
                            segundos = total_segundos % 60

                            dato = f"{horas:02}:{minutos:02}:{segundos:02}"

                        fila_limpia.append(dato)

                    print(tuple(fila_limpia))

    except Error as e:
        print("Error:", e)

    finally:
        if conexion and conexion.is_connected():
            cursor.close()
            conexion.close()
            print("\nConexión cerrada.")

if __name__ == "__main__":
    consultar_tablas()