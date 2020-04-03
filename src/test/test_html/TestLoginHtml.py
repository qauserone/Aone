import unittest
from src.act.html.LoginHtml import LoginHtml


class TestLoginHtml(unittest.TestCase, LoginHtml):


    def test_login_html(self):
        self.try_login_html()

if __name__ == '__main__':
    unittest.main()
