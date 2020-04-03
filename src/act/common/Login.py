import allure
from src.Aone import Aone


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
