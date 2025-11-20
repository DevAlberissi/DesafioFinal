import unittest
from app import app
import werkzeug

# Patch temporário para adicionar o atributo '__version__' em werkzeug
# (Mantido do seu código original)
if not hasattr(werkzeug, '__version__'):
    werkzeug.__version__ = "mock-version"

class APITestCase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        # Criação do cliente de teste
        cls.client = app.test_client()
        cls.client.testing = True

    def test_home_route(self):
        response = self.client.get('/')
        self.assertEqual(response.status_code, 200)
        # Assumindo que a rota home retorna uma mensagem específica
        self.assertEqual(response.json, {"message": "API is running"})
        """
        Teste 1: Verifica se a rota principal (/) está online.
        """

    def test_login_route_success(self):
        response = self.client.post('/login')
        self.assertEqual(response.status_code, 200)
        self.assertIn('access_token', response.json)
        """
        Teste 2: Verifica se a rota /login (com POST) funciona
        e retorna um token de acesso.
        """

    def test_protected_route_no_token(self):
        response = self.client.get('/protected')            
        self.assertEqual(response.status_code, 401)  
        """
        Teste 3: Verifica se a rota /protected está realmente protegida,
        retornando 401 (Unauthorized) se nenhum token for enviado.
        """


if __name__ == '__main__':
    unittest.main()