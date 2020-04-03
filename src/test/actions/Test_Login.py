import unittest
from src.act.common.Login import Login
from src.utils.my_constants.html.Environment import Environment



class Test_Login(unittest.TestCase):

    def test_try_login(self):
        a = Login()
        a.try_login(Environment.URL_LOCALHOST)

if __name__ == '__main__':
    unittest.main()
