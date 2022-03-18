from unittest import TestCase
from app import app

from forex_python.converter import RatesNotAvailableError

app.config['TESTING'] = True
app.config['DEBUG_TB_HOSTS'] = ['dont-show-debug-toolbar']

class ConverterTestCase(TestCase):
    def test_show_form(self):
        """test home route, show form """
        with app.test_client() as client:
            res = client.get("/")
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<h1>Forex Converter</h1>', html)
    def test_post_form(self):
        """test /calculate-route, data post generate conversion result """
        with app.test_client() as client:
            res = client.post('/calculate-rate',data={"from":"USD","to":"EUR","amt":"100"})
            html = res.get_data(as_text=True)
            self.assertEqual(res.status_code, 200)
            self.assertIn('<p class="result">€90.49</p>', html)
    def test_post_code_err(self):
        """test wrong currency code, flash message error """
         with app.test_client() as client:
             res = client.post('/calculate-rate',data={"from":"WRONGCODE","to":"EUR","amt":"100"}, follow_redirects=True)
             html = res.get_data(as_text=True)
             self.assertEqual(res.status_code, 200)
             self.assertIn('<h4 class="err_code">NOT a valid Currency Code</h4>', html)
    def test_post_amt_err(self):
        """testing wrong amount, flash message error"""
         with app.test_client() as client:
             res = client.post('/calculate-rate',data={"from":"USD","to":"EUR","amt":"ABC"}, follow_redirects=True)
             html = res.get_data(as_text=True)
             self.assertEqual(res.status_code, 200)
             self.assertIn('<h4 class="err_amt">NOT a valid amount</h4>', html)


