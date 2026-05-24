import unittest
from app import app

class TestApp(unittest.TestCase):
    def setUp(self):
        # Configuramos el cliente de pruebas de Flask
        self.app = app.test_client()
        self.app.testing = True

    def test_hello_world(self):
        # Hacemos una peticion GET a la raiz '/'
        response = self.app.get('/')
        # Verificamos que responda con 200 OK
        self.assertEqual(response.status_code, 200)
        # Verificamos que el texto 'Hola Mundo' este en la respuesta
        self.assertIn(b"Hola Mundo", response.data)

    def test_add(self):
        # Hacemos una peticion a la ruta de suma
        response = self.app.get('/add/2/3')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"5.0", response.data)

    def test_add_invalid(self):
        # Probamos con parametros invalidos
        response = self.app.get('/add/dos/tres')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b"Error", response.data)

if __name__ == '__main__':
    unittest.main()
