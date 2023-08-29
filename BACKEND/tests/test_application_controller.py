import json
import unittest
from app import create_app
from app.services.decision_engine_service import submit_application


class TestApplicationController(unittest.TestCase):

    def setUp(self):
        self.app = create_app().test_client()

    def test_submit_application(self):
        application_data = {
            "businessName": "Example Business",
            "yearEstablished": "2010",
            "loanAmount": 50000,
            "selectedYear": 2020,
            "selectedMonth": 12,
            "profitOrLossSummary": [
                {
                    "year": 2020,
                    "month": 12,
                    "profitOrLoss": 1000,
                    "assetsValue": 30000
                },
                {
                    "year": 2020,
                    "month": 11,
                    "profitOrLoss": -500,
                    "assetsValue": 28000
                }
            ]
        }
        response = self.app.post('/application/submit', json=application_data)
        self.assertEqual(response.status_code, 200)
        data = json.loads(response.data)
        self.assertEqual(data['applicationStatus'], 'Approved')


if __name__ == '__main__':
    unittest.main()
