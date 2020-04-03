import allure
from src.act.common.Login import Login
from src.test.functional.local_html.po.poLogin import poLogin
from src.test.functional.local_html.po.poLogin_target import poLogin_target
from src.utils.my_constants.localhost.Environment import Environment
from src.utils.my_constants.localhost.Users import Users

class Find_id(Login):

    @allure.step
    def login_and_find_id(self, url, user, passw, xpath_user, xpath_passw, xpath_cmd, xpath_target, id):
        self.login(url, user, passw, xpath_user, xpath_passw, xpath_cmd, xpath_target)
        self.find_id(id)

    def find_id(self, xpath_input, id):
        self.visibility_element(xpath_input)
        self.send_keys(xpath_input, id)
        self.log.info(id)

