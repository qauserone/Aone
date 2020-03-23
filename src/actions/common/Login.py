import allure
from src.Aone import Aone
from src.test.functional.local_html.po.poLogin import poLogin
from src.test.functional.local_html.po.poLogin_target import poLogin_target
from src.utils.my_constants.localhost.Environment import Environment
from src.utils.my_constants.localhost.Users import Users

class Login(Aone):


    @allure.step
    def login(self, url, user, passw, xpath_user, xpath_passw, xpath_cmd, xpath_target):
        self.open_url(url)
        self.complete_user(xpath_user, user)
        self.complete_passw(xpath_passw, passw)
        self.select_cmd(xpath_cmd)
        self.verify_element_target(xpath_target)

    @allure.step
    def open_url(self, url):
        self.open_browser(url)

    @allure.step
    def complete_user(self, xpath, user):
        self.send_keys(xpath, user)

    @allure.step
    def complete_passw(self, xpath, passw):
        self.send_keys(xpath, passw)

    @allure.step
    def select_cmd(self, xpath):
        self.select_element(xpath)

    @allure.step
    def verify_element_target(self, xpath):
        self.select_element(xpath)


# a = Login()
# a.login(Environment.URL_LOCALHOST,Users.USER_DEFAULT, Users.PASSW, poLogin.INPUT_USER,poLogin.INPUT_PASSW,poLogin.CMD, poLogin_target.TARGET)
# a.close_browser()