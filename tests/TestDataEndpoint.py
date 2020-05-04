import unittest
from app import app


class MyTestCase(unittest.TestCase):
    def test_something(self):
        response = app.test_client().post('/data', headers={"Content-Type": "application/json"}, data={})
        data = response.json['response']
        code = response.status_code
        self.assertEqual(code, 200)

    def test_something_else(self):
        response = app.test_client().post('/data', headers={"Content-Type": "application/json"}, data={})
        data = response.json['response']
        code = response.status_code
        self.assertEqual(data, "Successful")


if __name__ == '__main__':
    unittest.main()
