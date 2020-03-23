import pytest
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait 
from selenium.webdriver.support import expected_conditions as EC 
from selenium.common.exceptions import TimeoutException
from src.utils.constants.english_message import MsgSearch


class Search():


    def visibility(self, xpath, to=2):
        """
        Method to wait for an element to be visible
        :param xpath: String. Xpath of searched element
        :param to: Integer. Timeout
        """
        try:
            wait = WebDriverWait(self.driver, to)
            wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
            totalWait = 0
            while (totalWait < 0.01):
                self.wait(0.01)
                totalWait = totalWait + 0.01
        except TimeoutException:
            # self.get_screenshot()
            self.log.warning(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(xpath))
            return False
        # self.highlight(xpath)
        self.log.info(MsgSearch.MSG_SEARCH_ELEM.format(xpath))
        return True

    # def visibility_element(self, xpath, to=2):
    #     """
    #     Method to wait for an element to be visible
    #     :param xpath: String. Xpath of searched element
    #     :param to: Integer. Timeout
    #     """
    #     try:
    #         wait = WebDriverWait(self.driver, to)
    #         wait.until(EC.visibility_of_element_located((By.XPATH, xpath)))
    #         totalWait = 0
    #         while (totalWait < 0.01):
    #             self.wait(0.01)
    #             totalWait = totalWait + 0.01
    #     except TimeoutException:
    #         # self.get_screenshot()
    #         self.log.warning(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(xpath))
    #         return False
    #     # self.highlight(xpath)
    #     self.log.info(MsgSearch.MSG_SEARCH_ELEM.format(xpath))
    #     return True

    def wait(self, secs):
        time.sleep(secs)

    def verify(self, verify_xpath, to=7):
        if self.visibility_element(verify_xpath, to):
                return True
        else:
                return False

    def be_clickable(self, xpath, to=2):
        """
        Method to wait for an element to be clickable
        :param xpath: String. Xpath of searched element
        :param to: Integer. Timeout
        """
        try:
            wait = WebDriverWait(self.driver, to)
            wait.until(EC.element_to_be_clickable((By.XPATH, xpath)))
            totalWait = 0
            while (totalWait < 0.01):
                self.wait(0.01)
                totalWait = totalWait + 0.01
        except TimeoutException:
            self.log.error(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(xpath))
            return False
        return True

    def search_element_by_xpath(self, xpath):
        """
        Method to search an element by xpath
        :param xpath: String. Xpath of searched element
        :return: WebElement.
        """
        return self.search_element_by(By.XPATH, xpath)
    
    def search_element_by_id(self, id):
        """
        Method to search an element by id
        :param xpath: String. Xpath of searched element
        :return: WebElement.
        """
        return self.search_element_by(By.ID, id)
    
    def search_element_by(self, by, value):
        self.log.info(MsgSearch.MSG_SEARCH_ELEM_BY.format(by, value))
        return self.driver.find_element(by, value)

    def search_elements(self, xpath, to): 
        """
        Method to get all elements present by xpath
        :param xpath: String. Elements to search
        :param to: Integer. Timeout
        :return: list of WebElement
        """
        if self.visibility_element(xpath, to):
            elems= self.driver.find_elements_by_xpath(xpath)
            self.log.info(MsgSearch.MSG_SEARCH_ELEMS.format(
                                                        len(elems), xpath))
            return elems
        else:
            return None

    def double_visibility_element(self, xpath1, xpath2, timeout):
        """
        Method to wait two element.
        :param xpath1: String. First element to wait
        :param xpath2: Strign. Second element to wait
        :param timeout: Integer. Timeout
        :return: True if find first element.
                 False if find second element.
                 None if none of elements is found
        """
        self.log.info(MsgSearch.MSG_DOUBLE_SEARCH)
        while timeout > 0:
            if self.visibility_element(xpath1, 1):
                return True
            elif self.visibility_element(xpath2, 1):
                return False
            timeout -= 1
        self.log.error(MsgSearch.MSG_DOUBLE_SEARCH_ERROR)
        pytest.fail(MsgSearch.MSG_DOUBLE_SEARCH_ERROR)

    def verifySelection(self,xpath,accion,to=7):
        """
        Method to check if an element if visible
        :param xpath: String. Xpath of the element
        :param accion: String. Description to attach in allure
        :param to: Integer. TimeOut
        """
        if self.visibility_element(xpath, to):
            self.capture_image(MsgSearch.MSG_VERIFY.format(accion))
            return True
        else:
            self.wait(2)
            self.capture_image(accion)
            self.log.error(MsgSearch.MSG_VERIFY_ERROR.format(accion))
            pytest.fail(accion)
            return False

    def verify_value(self,xpath,msgOk,msgFail,find_text,sleep=5):
        """
        Method to compare an element's text with a text
        :param xpath. String. Xpath of the searched element
        :param find_text: String. Expected text.
        :return: True. If text of element is same as the expected text
                 False. If text of element isn't same
        """
        self.wait(sleep)
        if self.visibility_element(xpath):
            value=self.get_element_text(xpath)
        else:
            pytest.fail(msgFail)
            return False
        
        self.capture_image(MsgSearch.DSC_COMPARE_TEXT.format(find_text, value))
        if value == find_text:
            self.log.info(MsgSearch.MSG_COMPARE_TEXT.format(find_text, xpath))
            return True
        else: 
            self.log.error(MsgSearch.MSG_COMPARE_TEXT_ERROR.format(
                                                            find_text, xpath))
            pytest.fail(msgFail)


    def checkFields(self,listaCampos,msgOk,msgFail):
        """
        Method to search many items in the browser
        :param listaCampos: list. List of xpath of searched element
        """
        listaOK=[]
        listaNoOk=[]
        for elem in listaCampos:
            if self.visibility_element(elem):
                listaOK.append(elem)
            else:
                listaNoOk.append(elem)

        if len(listaNoOk)>1:
            self.log.error(MsgSearch.MSG_CHECK_FIELD_ERROR)
            pytest.fail(msgFail)
            self.capturar_imagen(msgFail)
        else: 
            self.capturar_imagen(msgOk)
        self.log.info(MsgSearch.MSG_RESULT_CHECK_FIELD.format(len(listaCampos),
                                                    len(listaOK),
                                                    len(listaNoOk))) 
        

