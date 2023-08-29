import json
import unittest
from app import create_app
from app.services.accounting_service import fetch_balance_sheet


class TestBalanceSheetController(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def test_fetch_balance_sheet(self):
        request_data = {
            "year": 2020,
            "month": 12
        }
        response = self.app.post('/balance_sheet/fetch', json=request_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['year'], 2020)
        self.assertEqual(data['month'], 12)


if __name__ == '__main__':
    unittest.main()
