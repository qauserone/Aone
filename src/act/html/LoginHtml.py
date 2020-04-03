import allure
from src.act.common.Login import Login
from src.utils.my_constants.localhost.Environment import Environment
from src.utils.my_constants.localhost.Users import Users
from src.test.functional.local_html.po.poLogin import poLogin
from src.test.functional.local_html.po.poLogin_target import poLogin_target


@allure.feature()
class LoginHtml(Login):


    @allure.step
    def try_login_html(self):
        self.login(Environment.URL_LOCALHOST,
                       Users.USER_DEFAULT,
                       Users.PASSW,
                       poLogin.INPUT_USER,
                       poLogin.INPUT_PASSW,
                       poLogin.CMD,
                       poLogin_target.TARGET)
