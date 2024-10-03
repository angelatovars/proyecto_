import mysql.connector
from mysql.connector import Error
import hashlib

# Conexión a la base de datos
def conectar_db():
    try:
        connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",  # Cambia por tu contraseña
            database="my_database"     # Cambia por el nombre de tu base de datos
        )
        return connection
    except Error as err:
        print(f"Error al conectar a la base de datos: {err}")
        return None

# Hash de la contraseña
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Crear usuario (C)
def crear_usuario(nombre_completo, email, password):
    hashed_password = hash_password(password)
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            insert_query = "INSERT INTO usuarios (nombre_completo, email, contraseña) VALUES (%s, %s, %s)"
            cursor.execute(insert_query, (nombre_completo, email, hashed_password))
            connection.commit()
            return True
        except Error as err:
            print(f"Error al registrar usuario: {err}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False

# Leer usuarios (R)
def obtener_usuarios():
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            select_query = "SELECT * FROM usuarios"
            cursor.execute(select_query)
            usuarios = cursor.fetchall()
            return usuarios
        except Error as err:
            print(f"Error al obtener usuarios: {err}")
            return []
        finally:
            cursor.close()
            connection.close()
    return []

# Actualizar usuario (U)
def actualizar_usuario(id, nombre_completo, email, password=None):
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            if password:
                hashed_password = hash_password(password)
                update_query = "UPDATE usuarios SET nombre_completo = %s, email = %s, contraseña = %s WHERE id = %s"
                cursor.execute(update_query, (nombre_completo, email, hashed_password, id))
            else:
                update_query = "UPDATE usuarios SET nombre_completo = %s, email = %s WHERE id = %s"
                cursor.execute(update_query, (nombre_completo, email, id))
            connection.commit()
            return True
        except Error as err:
            print(f"Error al actualizar usuario: {err}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False

# Eliminar usuario (D)
def eliminar_usuario(id):
    connection = conectar_db()
    if connection:
        try:
            cursor = connection.cursor()
            delete_query = "DELETE FROM usuarios WHERE id = %s"
            cursor.execute(delete_query, (id,))
            connection.commit()
            return True
        except Error as err:
            print(f"Error al eliminar usuario: {err}")
            return False
        finally:
            cursor.close()
            connection.close()
    return False
