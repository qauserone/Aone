import allure
from src.act.common.Login import Login
from src.utils.my_constants.localhost.Environment import Environment
from src.utils.my_constants.localhost.Users import Users
from src.test.functional.local_html.po.poLogin import poLogin
from src.test.functional.local_html.po.poLogin_target import poLogin_target


@allure.feature()
class MyLoginHtml(Login):


    def __init__(self):
        self.try_my_login()

    @allure.step
    def try_my_login(self):
        a = Login()
        a.login(Environment.URL_LOCALHOST,
                       Users.USER_DEFAULT,
                       Users.PASSW,
                       poLogin.INPUT_USER,
                       poLogin.INPUT_PASSW,
                       poLogin.CMD,
                       poLogin_target.TARGET)

# a = Login()
# a.login(Environment.URL_LOCALHOST,Users.USER_DEFAULT, Users.PASSW, poLogin.INPUT_USER,poLogin.INPUT_PASSW,poLogin.CMD, poLogin_target.TARGET)
# a.close_browser()
