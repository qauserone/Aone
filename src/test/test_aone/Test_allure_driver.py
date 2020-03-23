import unittest
from src.Aone import Aone
from src.utils.my_constants.localhost.Environment import Environment


class Test_allure_driver(unittest.TestCase):


    def test_open_chrome(self, url=Environment.URL_LOCALHOST):
        xpath_title = '//*[@id="contact"]/h3'
        xpath_cmd_submit = '//*[@id="contact-submit"]'
        a = Aone()
        a.open_chrome(url)
        a.send_keys('//*[@id="contact"]/fieldset[1]/input', 'userX')
        a.go_to_xpath('//*[@id="end_button"]')
        a.select_element('//*[@id="end_button"]')
        a.verify_element('//*[@id="end_button"]')
        a.close_browser()

if __name__ == '__main__':
    unittest.main()
