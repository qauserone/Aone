import allure
import unittest
from src.Aone import Aone
from src.utils.my_constants.localhost.Environment import Environment


class TestAone(unittest.TestCase, Aone):


    @allure.step
    def test_open_browser(self):
        self.open_browser(Environment.URL_LOCALHOST)

    @allure.step
    def test_visibility_element(self):
        self.open_browser(Environment.URL_LOCALHOST)
        self.visibility_element(xpath='//*[@id="contact"]/h3')

    @allure.step
    def test_select_element(self):
        self.open_browser(Environment.URL_LOCALHOST)
        xpath = '/html/body/div[1]/form/fieldset[1]/input'
        self.select_element(xpath)

    @allure.step
    def test_send_keys(self):
        self.open_browser(Environment.URL_LOCALHOST)
        xpath = '/html/body/div[1]/form/fieldset[1]/input'
        self.send_keys(xpath, 'abcdef')

    @allure.step
    def test_verify_elment(self):
        self.open_browser(Environment.URL_LOCALHOST)
        xpath = '/html/body/div[1]/form/fieldset[1]/input'
        self.verify_element(xpath)

if __name__ == '__main__':
    unittest.main()
