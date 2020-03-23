import pytest
from random import choice
from selenium.common.exceptions import (NoSuchElementException, 
                                        UnexpectedTagNameException)
from selenium.webdriver.support.select import Select
from src.utils.constants.english_message import MsgSelect, MsgSearch
from src.utils.constants.constants import ARIA_OWNS, TAG_LI, SCROLL


class Select():


    def obtain_select(self, xpath, to=10):
        """
        Method to obtain a select element. If the element isn't a select
        element, show an error in the log
        :param xpath: String. Xpath of the element
        :param to: Integer. Timeout
        """
        if self.visibility_element(xpath, to):
            try:
                select_elem = Select(self.driver.find_element_by_xpath(xpath))
                return select_elem
            except UnexpectedTagNameException:
                self.log.error(MsgSelect.MSG_SELECT_ELEMENT_ERROR.format(
                                                                    xpath))
                return None
        else:
            return None
        
    def select_by_text(self, xpath, text):
        """
        Select an option in a select element by text
        :param xpath: String. Xpath of element
        :param text: String. Text of searched option
        """
        select = self.obtain_select(xpath)
        if select is not None:
            select.select_by_visible_text(text)
            self.log.info(MsgSelect.MSG_SELECT_TEXT.format(text, xpath))
            return True
        else:
            return False
        
    def select_by_value(self, xpath, value):
        """
        Select an option in a select element by value
        :param xpath: String. Xpath of element
        :param value: String. Value of searched option
        """ 
        select = self.obtain_select(xpath)
        if select is None: 
            self.log.error(MsgSelect.MSG_SELECT_VALUE_ERROR,format(
                                                                value, xpath))
            return False
        else:
            select.select_by_value(value)
            self.log.info(MsgSelect.MSG_SELECT_VALUE.format(value, xpath))
            return True
        
    def select_by_index(self, xpath, index):
        """
        Select an option in a select element by index
        :param xpath: String. Xpath of element
        :param index: Integer. Index of searched option
        """
        select = self.obtain_select(xpath)
        if select is None:
            self.log.error(MsgSelect.MSG_SELECT_INDEX_ERROR.format(
                                                                index, xpath))
            return False
        else:
            select.select_by_index(index)
            self.log.info(MsgSelect.MSG_SELECT_INDEX.format(index, xpath))
            return True
        
    def select_random(self, xpath):
        """
        Method to select a random option from a select element
        :param xpath: String. Xpath of element
        """
        select = self.obtain_select(xpath)
        if select is None:
            return False
        else:
            options = select.options
            option = choice(options)
            self.log.info(MsgSelect.MSG_SELECT_RANDOM)
            self.select_by_value(xpath, option.get_attribute('value'))
            return True
        
    def select_option(self, xpath, msgOk, msgFail, to=5, option=None, arrow=None):
        """
        Method to select an option from dropdown. This method is used in case
        the element isn't a select element
        :param xpath: String. Xpath of the element
        :param to: Integer. Timeout
        :param option: String/Integer. 
                       If option is a string, then search by text of option.
                       If option is an int, then, search by index
        :param arrow: String. Xpath of arrow to select and expand dropbox
        """
        if self.visibility_element(xpath, to):
            elem = self.driver.find_element_by_xpath(xpath)
        else:
            pytest.fail(msgFail)
            return False
        
        if arrow is None:
            elem.click()
        else:
            self.selectElement(arrow, msgOk, msgFail, to)
        self.wait(.5)
        options_table_id = self.get_attribute(xpath, ARIA_OWNS)
        # Se trata de obtener el cuadro de opciones del dropdown
        try:
            options_table = self.search_element_by_id(options_table_id)
        except NoSuchElementException:
            msg = MsgSearch.MSG_SEARCH_ELEM_ERROR.format(options_table_id)
            self.capture_image(msg, to)
            pytest.skip(msg)
        options= options_table.find_elements_by_tag_name(TAG_LI)
        flag = False
        if type(option) is int:
            indice = option
            flag = True
        elif type(option) is str or type(option) is unicode:
            str_options = [x.text for x in options]
            try:
                indice = str_options.index(option)
                flag = True
            except ValueError:
                self.log.error(MsgSelect.MSG_SELECT_OPTION_ERROR.format(
                                                                    option))
                pytest.fail(MsgSelect.MSG_SELECT_OPTION_ERROR.format(option)) 
        if flag:
            try:
                opcion = options[indice]
            except IndexError:
                self.log.error(MsgSelect.MSG_SELECT_INDEX_ERROR)
            self.driver.execute_script(SCROLL, opcion)
            opcion.click()
            self.log.info(MsgSelect.MSG_SELECT_OPTION.format(
                                                        opcion.text, xpath))
        else:
            msg = MsgSelect.MSG_SELECT_OPTION_ERROR.format(option)
            self.capture_image(msg, to)
            pytest.fail(msg)

    
    def selectListByPartialText(self,xpath,find_text):
        """
        Method to select an option from select element, by partial text
        :param xpath: String. Xpath of the element
        :param find_text: String. Text to search
        """
        if self.visibility_element(xpath, 10):
            select = self.obtain_select(xpath)
        else:
            pytest.skip(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(find_text))
            return False
        
        options = select.options
        index = None
        for option in options:
            if find_text in option.text and option.is_enabled():
                index = options.index(option)
                break
        if index is None:
            self.log.error(MsgSelect.MSG_SELECT_OPTION_ERROR)
            pytest.skip(MsgSearch.MSG_SEARCH_ELEM_ERROR.format(find_text))
            return False
        else:
            select.select_by_index(index)
            selected_option = select.first_selected_option
            self.log.info(MsgSelect.MSG_SELECT_OPTION.format(
                                                selected_option.text,xpath))
            return True
