import allure
import unittest
from src.act.common.Login import Login
from src.utils.my_constants.localhost.Environment import Environment
from src.utils.my_constants.localhost.Users import Users
from src.test.functional.local_html.po.poLogin import poLogin
from src.test.functional.local_html.po.poLogin_target import poLogin_target

@allure.feature()
class TestLogin(unittest.TestCase):

    @allure.step
    def test_login_html(self):
        a = Login()
        a.login(Environment.URL_LOCALHOST, Users.USER_DEFAULT, Users.PASSW, poLogin.INPUT_USER, poLogin.INPUT_PASSW,
                poLogin.CMD, poLogin_target.TARGET)
        a.close_browser()

if __name__ == '__main__':
    unittest.main()
