import allure
from src.actions.common.Login import Login
from src.test.functional.local_html.po.poLogin import poLogin
from src.test.functional.local_html.po.poLogin_target import poLogin_target
from src.utils.my_constants.localhost.Environment import Environment
from src.utils.my_constants.localhost.Users import Users

class Find_id(Login):


    @allure.step
    def login_and_find_id(self, url, user, passw, xpath_user, xpath_passw, xpath_cmd, xpath_target, id):
        self.login(url, user, passw, xpath_user, xpath_passw, xpath_cmd, xpath_target)
        self.find_id(id)

    def find_id(self, url, xpath_input, xpath_cmd, id):
        self.open_browser(url)
        self.select_element(xpath_input)
        self.send_keys(xpath_input, id)
        self.log.info(id)

a = Find_id()
xpath_input = "//input[@class='gLFyf gsfi']"
xpath_cmd="//div[@class='FPdoLc tfB0Bf']/center[1]/input[@class='gNO89b' and 1]"

a.find_id("https://www.google.com.ar/", xpath_input, xpath_cmd, id=1234)
# a.login_and_find_id(Environment.URL_LOCALHOST, Users.USER_DEFAULT, Users.PASSW,
#                     poLogin.INPUT_USER, poLogin.INPUT_PASSW,poLogin.CMD, poLogin_target.TARGET, id=4321)
# a.close_browser()
a