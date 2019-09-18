import unittest
import requests


class TestApiYandex(unittest.TestCase):
    api_key = 'trnsl.1.1.20190918T060754Z.ae3caa7ba03d1b8c.c14ea87f8753ae8deeeb90e2f57693baf2098f42'
    url = 'https://translate.yandex.net/api/v1.5/tr.json/translate'

    def setUp(self) -> None:
        self.session = requests.Session()
        self.params = {'key': self.api_key, 'lang': 'en-ru', 'text': 'hi'}

    def test_api_request(self):
        response = self.session.post(self.url, params=self.params)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.json()['text'][0], 'привет')


if __name__ == '__main__':
    unittest.main()
