from unittest import TestCase
from service import app
from service.models import Account

class TestAccountService(TestCase):
    """Test Cases untuk REST API Accounts Service"""

    def setUp(self):
        """Berjalan sebelum setiap test"""
        self.client = app.test_client()
        Account.data.clear()
        Account.index = 0

    def tearDown(self):
        """Berjalan setelah setiap test"""
        Account.data.clear()

    def test_health(self):
        """Test untuk endpoint /health"""
        resp = self.client.get("/health")
        self.assertEqual(resp.status_code, 200)
        self.assertEqual(resp.get_json()["status"], "OK")

    def test_create_account(self):
        """Test membuat akun baru"""
        new_account = {"name": "John Doe", "email": "john@example.com"}
        resp = self.client.post(
            "/accounts",
            json=new_account,
            content_type="application/json"
        )
        self.assertEqual(resp.status_code, 201)
        data = resp.get_json()
        self.assertEqual(data["name"], "John Doe")
        self.assertEqual(data["email"], "john@example.com")