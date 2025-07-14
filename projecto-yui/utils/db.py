import sqlite3  # Librería para manejar SQLite en Python
import os       # Para trabajar con rutas de carpetas y archivos

def crear_bd_usuario(nombre_usuario):
    # Ruta base donde están las BD
    carpeta_base = os.path.join("user-database", "usuario") 

    if not os.path.exists(carpeta_base): 
        os.makedirs(carpeta_base) 

    # Ruta completa del archivo .db
    ruta_db = os.path.join(carpeta_base, f"{nombre_usuario}.db") # 

    # Si el archivo no existe, lo creamos y le ponemos una tabla
    if not os.path.exists(ruta_db): #.exists() comprueba si el archivo ya existe
        conexion = sqlite3.connect(ruta_db) 
        cursor = conexion.cursor() # 

        # Crear la tabla donde guardaremos las interacciones
        cursor.execute("""
            CREATE TABLE interacciones (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                entrada TEXT,
                emocion TEXT,
                respuesta TEXT
            )
        """)

        conexion.commit()
        conexion.close()
        print(f"🆕 Base de datos creada para {nombre_usuario}")
    else:
        print(f"✅ Base de datos cargada para {nombre_usuario}")

    return ruta_db  # Devolvemos la ruta para usarla después

def listar_usuarios():
    carpeta_base = os.path.join("user-database", "usuario")
    if not os.path.exists(carpeta_base):
        return []  # No hay usuarios aún

    archivos = os.listdir(carpeta_base)
    usuarios = [archivo.replace(".db", "") for archivo in archivos if archivo.endswith(".db")]
    return usuarios