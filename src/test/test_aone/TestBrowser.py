import allure
import unittest
from src.Aone import Aone
from src.utils.my_constants.localhost.Environment import Environment

@allure.feature()
class TestBrowser(unittest.TestCase):

    @allure.step
    def test_count_method_class(self):
        print('count method class by name')
        pass

    @allure.step
    def test_open_chrome(self, url=Environment.URL_LOCALHOST):
        a = Aone()
        a.open_chrome(url)
        a.close_browser()

    @allure.step
    def test_open_firefox(self):
        a = Aone()
        a.open_firefox(Environment.URL_LOCALHOST)

    @allure.step
    def test_ie(self, url=Environment.URL_LOCALHOST):
        a = Aone()
        a.open_ie(url)
        a.close_browser()

    @allure.step
    def test_open_firefox_w_propertys(self):
        a = Aone()
        a.open_firefox_w_prop(url=Environment.URL_LOCALHOST)
        a.close_browser()

    @allure.step
    def test_open_chrome_w_propertys(self):
        a = Aone()
        a.open_chrome_w_prop(url=Environment.URL_LOCALHOST)
        a.close_browser()

    @allure.step
    def test_mobile_emulation(self, url=Environment.URL_LOCALHOST):
        a=Aone()
        a.mobile_emulation(url)
        xpath = '/html/body/div[1]/form/fieldset[1]/input'
        a.visibility_element(xpath)
        a.select_element(xpath)
        # a.close_browser()

    @allure.step
    def test_open_browser(self):
        a = Aone()
        a.open_browser(browser='chrome', url=Environment.URL_LOCALHOST)
        a.close_browser()

    @allure.step
    def test_open_browser_and_get_tabs(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.get_tabs()
        a.close_browser()

    @allure.step
    def test_open_browser_and_new_tabs(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.new_tab()
        a.close_browser()

    @allure.step
    def test_open_browser_and_change_tab(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.new_tab()
        a.change_tab(1)
        a.close_browser()

    @allure.step
    def test_open_browser_and_close_tab(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.new_tab()
        a.change_tab(1)
        a.close_tab()
        a.close_browser()

    @allure.step
    def test_open_browser_and_back(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.new_tab()
        a.change_tab(1)
        a.back()
        a.close_tab()
        a.close_browser()

    @allure.step
    def test_open_browser_and_forward(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.new_tab()
        a.change_tab(1)
        a.forward()
        a.close_tab()
        a.close_browser()

    @allure.step
    def test_open_browser_and_get_windows_size(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.get_windows_size()
        a.close_browser()

    @allure.step
    def test_open_browser_and_set_windows_size(self, width, height):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.set_windows_size(width, height)
        a.close_browser()

    @allure.step
    def test_open_browser_and_get_url(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.get_url()
        a.close_browser()

    @allure.step
    def test_open_browser_and_refresh_page(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.get_url()
        a.refresh_page()
        a.close_browser()

    @allure.step
    def test_open_browser_and_get_html(self):
        a = Aone()
        a.open_chrome(url=Environment.URL_LOCALHOST)
        a.get_html()
        a.close_browser()

if __name__ == '__main__':
    unittest.main()
