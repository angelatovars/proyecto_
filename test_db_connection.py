    import unittest
    from db_connection import verificar_usuario, registrar_usuario, conectar

    class TestDBConnection(unittest.TestCase):
        def setUp(self):
            # Configuración de la base de datos para pruebas
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios (
                                id INTEGER PRIMARY KEY AUTOINCREMENT,
                                nombre_completo TEXT NOT NULL,
                                email TEXT NOT NULL UNIQUE,
                                password TEXT NOT NULL
                            )''')
            conn.commit()
            conn.close()

        def tearDown(self):
            # Limpieza de la base de datos después de las pruebas
            conn = conectar()
            cursor = conn.cursor()
            cursor.execute("DROP TABLE usuarios")
            conn.commit()
            conn.close()

        def test_registrar_usuario(self):
            result = registrar_usuario("Test User", "testuser@example.com", "password123")
            self.assertTrue(result)

        def test_verificar_usuario(self):
            registrar_usuario("Test User", "testuser@example.com", "password123")
            result = verificar_usuario("testuser@example.com", "password123")
            self.assertTrue(result)
            result = verificar_usuario("testuser@example.com", "wrongpassword")
            self.assertFalse(result)

    if __name__ == '__main__':
        unittest.main()
