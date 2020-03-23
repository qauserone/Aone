import pytest
from selenium.webdriver.common.action_chains import ActionChains
from src.utils.constants.english_message import MsgMouse


class Mouse():


    def select(self, xpath, to=5):
        """
        Method to click an element
        :param xpath: String. Xpath of element
        :param to: Integer. Timeout
        :return: Boolean
        """
        if self.be_clickable(xpath,to):
            self.search_element_by_xpath(xpath).click()
            return True
        else:
            return False



    def selectElement(self,xpath,msgOk,msgFail,to=5):
        if self.visibility_element(xpath, to):
        #if self.select(xpath,to):
            self.select(xpath, to)
            self.log.info(MsgMouse.MSG_CLICK_ELEM.format(xpath))
            return True
        else:
            self.log.error(MsgMouse.MSG_CLICK_ELEM_ERROR.format(xpath))
            return False
            pytest.fail(msgFail)
    
    def selectElement_highlight(self,xpath,msgOk,msgFail,sleep=5):
        if self.visibility_element(xpath,sleep):
            self.highlight(xpath, msgOk,sleep)
            self.select(xpath)
            self.log.info(MsgMouse.MSG_CLICK_ELEM.format(msgOk))
            return True
        else:
            self.log.error(MsgMouse.MSG_CLICK_ELEM_ERROR.format(xpath))
            pytest.fail(msgFail)
            return False

    def doubleClick(self, xpath):
        """
        Method to do double click on an element
        :param xpath: String. Xpath of the searched element
        """
        if self.visibility_element(xpath, 10):
            elem = self.search_element_by_xpath(xpath)
            actionChains = ActionChains(self.driver)
            actionChains.double_click(elem).perform()
            self.log.info(MsgMouse.MSG_DOUBLE_CLICK.format(xpath))
            return True
        else:
            return False
    
    def drag_and_drop(self, xpath, target_xpath):
        """
        Method to drag and drop an element in other element
        :param xpath: String. Xpath of the source element
        :param target_xpath: String. Xpath of the target element
        """
        to = 10
        source = self.visibility_element(xpath, to)
        target = self.visibility_element(target_xpath, to)
        if source and target:
            action_chains = ActionChains(self.driver)
            source = self.search_element_by_xpath(xpath)
            target = self.search_element_by_xpath(target_xpath)
            action_chains.drag_and_drop(source, target)
            self.log.info(MsgMouse.MSG_DRAG_DROP.format(xpath, target_xpath))
            return True
        else:
            return False


