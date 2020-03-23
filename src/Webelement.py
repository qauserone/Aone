from src.utils.constants.english_message import MsgWebelement


class Webelement():


    def get_attribute(self, xpath, attribute):
        """
        Method to obtain an attribute from an element
        :param xpath: String. Xpath of element.
        :param attribute: String. Attribute name
        """
        if self.visibility_element(xpath, 10):
            elem = self.driver.find_element_by_xpath(xpath)
        else:
            return False
        
        atr = elem.get_attribute(attribute)
        if atr is None or atr == '': 
            self.log.error(MsgWebelement.MSG_ATTRIBUTE_ERROR.format(
                                                           attribute, xpath))
        else:
            self.log.info(MsgWebelement.MSG_ATTRIBUTE.format(
                                                    atr, xpath, attribute))
            return atr
    
    def get_element_text(self, xpath):
        """
        Get text of a webElement
        :param xpath: String. Xpath of the element
        :return: String. Text of the searched element
        """
        if self.visibility_element(xpath, 10):
            text = self.driver.find_element_by_xpath(xpath).text
            self.log.info(MsgWebelement.MSG_GET_TEXT.format(xpath, text))
            return text
        else:
            return None
    
    def get_location(self, xpath):
        """
        Get the coordinate of the searched element
        :param xpath: String. Xpath of the element
        :return: float, float. Return x and y value
        """
        if self.visibility_element(xpath, 10):
            elem = self.search_element_by_xpath(xpath)
            location = elem.location
            self.log.info(MsgWebelement.MSG_GET_LOCATION.format(xpath, 
                                                                location))
            return location.get('x'), location.get('y')
        else:
            return None, None
    
    def get_size(self, xpath):
        """
        Get the size of the searched element
        :param xpath: String. Xpath of the element
        :return: float, float. Return height and width value
        """
        if self.visibility_element(xpath, 10):
            elem = self.search_element_by_xpath(xpath)
            size = elem.size
            self.log.info(MsgWebelement.MSG_GET_SIZE.format(xpath, size))
            return size.get('height'), size.get('width')
        else:
            return None, None        

    def is_displayed(self, xpath):
        """
        Method to ask if an element is displayed
        :param xpath: String. Xpath of the element.
        :return: Boolean
        """
        displayed = self.search_element_by_xpath(xpath).is_displayed()
        if displayed:
            self.log.info(MsgWebelement.MSG_DISPLAYED.format(xpath))
        else:
            self.log.warning(MsgWebelement.MSG_DISPLAYED_ERROR.format(xpath))  
        return displayed
    
    def is_enabled(self, xpath):
        """
        Method to ask if an element is enabled
        :param xpath: String. Xpath of the element.
        :return: Boolean
        """
        enabled = self.search_element_by_xpath(xpath).is_enabled()
        if enabled:
            self.log.info(MsgWebelement.MSG_ENABLED.format(xpath))
        else:
            self.log.warning(MsgWebelement.MSG_ENABLED_ERROR.format(xpath)) 
        return enabled

    def is_selected(self, xpath):
        """
        Method to ask if an element is selected
        :param xpath: String. Xpath of the element.
        :return: Boolean
        """
        selected = self.search_element_by_xpath(xpath).is_selected() 
        if selected:
            self.log.info(MsgWebelement.MSG_SELECTED.format(xpath))
        else:
            self.log.warning(MsgWebelement.MSG_SELECTED_ERROR.format(xpath))
        return selected

    def get_tag_name(self, xpath):
        """
        Method to obtain tag name from an element
        :param xpath: String. Xpath of the element
        :return: String
        """
        return self.search_element_by_xpath(xpath).tag_name

