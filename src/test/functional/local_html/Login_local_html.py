from src.act.common.Login import Login
from src.constants.Environment import Environment
from src.test.functional.local_html.po.poLogin import poLogin
from src.test.functional.local_html.po.poLogin_target import poLogin_target

class Login_local_html(Login):

    def try_login_html(self):

        url = Environment.URL_LOCALHOST
        poPage = poLogin()
        poPage_target = poLogin_target()

        self.try_login(url, poPage, 'usuarioX', '******1234******', poPage_target)



a = Login_local_html()
a.try_login_html()