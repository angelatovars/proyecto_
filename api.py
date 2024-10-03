from flask import Flask, request, jsonify
from db_connection import conectar_db

app = Flask(__name__)

# Crear usuario (POST)
@app.route('/usuarios', methods=['POST'])
def crear_usuario():
    data = request.json
    nombre_completo = data['nombre_completo']
    email = data['email']
    password = data['password']

    connection = conectar_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("INSERT INTO usuarios (nombre_completo, email, contraseña) VALUES (%s, %s, %s)", (nombre_completo, email, password))
            connection.commit()
            return jsonify({'message': 'Usuario creado exitosamente'}), 201
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        finally:
            cursor.close()
            connection.close()

# Obtener todos los usuarios (GET)
@app.route('/usuarios', methods=['GET'])
def obtener_usuarios():
    connection = conectar_db()
    if connection:
        cursor = connection.cursor()
        cursor.execute("SELECT id, nombre_completo, email FROM usuarios")
        usuarios = cursor.fetchall()
        cursor.close()
        connection.close()
        return jsonify(usuarios), 200
    return jsonify({'error': 'Error al conectar con la base de datos'}), 500

# Actualizar usuario (PUT)
@app.route('/usuarios/<int:id>', methods=['PUT'])
def actualizar_usuario(id):
    data = request.json
    nombre_completo = data['nombre_completo']
    email = data['email']
    password = data.get('password', None)

    connection = conectar_db()
    if connection:
        cursor = connection.cursor()
        try:
            if password:
                cursor.execute("UPDATE usuarios SET nombre_completo=%s, email=%s, contraseña=%s WHERE id=%s", (nombre_completo, email, password, id))
            else:
                cursor.execute("UPDATE usuarios SET nombre_completo=%s, email=%s WHERE id=%s", nombre_completo, email, id)
            connection.commit()
            return jsonify({'message': 'Usuario actualizado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        finally:
            cursor.close()
            connection.close()

# Eliminar usuario (DELETE)
@app.route('/usuarios/<int:id>', methods=['DELETE'])
def eliminar_usuario(id):
    connection = conectar_db()
    if connection:
        cursor = connection.cursor()
        try:
            cursor.execute("DELETE FROM usuarios WHERE id=%s", (id,))
            connection.commit()
            return jsonify({'message': 'Usuario eliminado exitosamente'}), 200
        except Exception as e:
            return jsonify({'error': str(e)}), 400
        finally:
            cursor.close()
            connection.close()

if __name__ == '__main__':
    app.run(debug=True)