from src.utils.constants.english_message import MsgMouse, MsgSearch, MsgKeyboard
from src.utils.constants.constants import (
    SAFEBROWSING, AUTOLOGIN, N_TRUSTED_URIS, AUTOMATIC_NTLM,
    N_DELEGATION, DOMAIN, PROXY, BINARY, IGNORE_CERTIFICATE, CHROME, FIREFOX,
    CHROME_P, FIREFOX_P
)
import allure
import pytest
from src.log import log
from src.Browser import Browser
from src.Search import Search
from src.Image import Image
from src.Allure_driver import Allure_driver
from src.Error_management import Errors
from src.Js import Js
from src.Keyboard import Keyboard
from src.Mouse import Mouse
from src.Select import Select
from src.Webelement import Webelement


class Aone(Allure_driver, Browser, Errors, Image, Js, Keyboard, log, Mouse, Search, Select, Webelement):

    def aone(self):
        pass

    @allure.step
    def open_browser(self, url, browser='chrome'):
        """
        Open the browser
        :param naveg: String. Name of browser
        :param url: String. Url to open
        """
        if browser.lower() == CHROME:
            self.open_chrome(url)
        elif browser.lower() == FIREFOX:
            self.open_firefox(url)
        elif browser.lower() == FIREFOX_P:
            self.open_firefox_w_prop(url)
        if browser.lower() == CHROME_P:
            self.open_chrome_w_prop(url)

    @allure.step
    def visibility_element(self, xpath):
        if self.visibility(xpath):
            # self.highlight(xpath)
            self.screenshot()
            return True
        else:
            self.screenshot()
            return False

    @allure.step
    def select_element(self, xpath, to=5):
        if self.visibility_element(xpath):
            self.driver.find_element_by_xpath(xpath).click()
            self.log.info(MsgMouse.MSG_CLICK_ELEM.format(xpath))
            return True
        else:
            self.log.error(MsgMouse.MSG_CLICK_ELEM_ERROR.format(xpath))
            return False

    @allure.step
    def verify_element(self, xpath, to=5):
        if self.visibility(xpath):
            # if self.select(xpath, to):
            self.visibility_element(xpath)
            self.log.info(MsgSearch.MSG_VERIFY.format(xpath))
            return True
        else:
            self.screenshot()
            self.log.error(MsgSearch.MSG_VERIFY_ERROR.format(xpath))
            pytest.fail(MsgSearch.MSG_VERIFY_ERROR.format(xpath))
            return False

    @allure.step
    def send_keys(self, xpath, text):
        """
        Method to write a text in a input.
        :param xpath: String. Xpath of the searched element.
        :param text: String/Integer. Text to input
        :param to: Integer. Timeout
        """
        if self.visibility(xpath):
            self.clear(xpath)
            self.search_element_by_xpath(xpath).send_keys(text)
            self.visibility_element(xpath)
            self.log.info(MsgKeyboard.MSG_INPUT.format(xpath, text))
            return True
        else:
            pytest.fail(MsgKeyboard.MSG_INPUT_KEY_ERROR.format(xpath))
            return False
