import pytest
from src.utils.constants.english_message import MsgMouse, MsgJS
from src.utils.constants.constants import (
    CLICK, SCROLL, SET_ATTRIBUTE, STYLE, BORDER, NEW_TAB, BACK
)
                                 

class Js():

    def highlight(self, xpath):
        """
        Method to highlight an element
        :param xpath: String. Xpath of searched element
        :param description: String. Description of screenshot
        """
        def apply_style(s):
            """ Method to apply a style for highlight """
            self.driver.execute_script(SET_ATTRIBUTE, objeto, s)
        objeto = self.driver.find_element_by_xpath(xpath)
        estilo_original = objeto.get_attribute(STYLE)
        apply_style(BORDER)
        self.wait(0.1)
        self.screenshot()
        apply_style(estilo_original)

    def selectElement_js(self,xpath, sleep=5):
        """ Method to click an element by js """
        if self.visibility_element(xpath, sleep):
            self.jsClick(xpath)
            self.log.info(MsgMouse.MSG_CLICK_ELEM.format(xpath))
            return True
        else:
            self.log.error(MsgMouse.MSG_CLICK_ELEM_ERROR.format(xpath))
            pytest.fail()
            return False

    def jsClick(self, xpath):
        """ Method to click an element by js """
        localizador = self.driver.find_element_by_xpath(xpath)
        self.driver.execute_script(CLICK, localizador)
    
    def go_to_xpath(self, xpath):
        """
        Method to scroll to searched element
        :param xpath: String. Xpath of searched element.
        """ 
        if self.visibility_element(xpath):
            locator = self.driver.find_element_by_xpath(xpath)
            self.driver.execute_script(SCROLL, locator)
            self.log.info(MsgJS.MSG_SCROLL.format(xpath))
            return True
        else:
            return False

    def create_tab_js(self, url):
        """
        Method to execute a js script to create a new tab in the browser
        :param url: String. URL for the new tab
        """
        self.driver.execute_script(NEW_TAB.format(url))
        self.log.info(MsgJS.MSG_CREATE_TAB.format(url))
        
    def back_js(self):
        """
        Method to return to a previous page
        """
        self.driver.execute_script(BACK)
        self.log.info(MsgJS.MSG_BACK)
