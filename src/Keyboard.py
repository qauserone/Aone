from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import InvalidElementStateException
from src.utils.constants.english_message import MsgKeyboard


class Keyboard():


    def send_key(self, xpath, key):
        """
        Method to enter a specific key by string
        :param key: String. Name of key to use
        """
        key_object = self.obtain_key(key)
        if key_object is not None:
            self.search_element_by_xpath(xpath).send_keys(key_object)
            self.log.info(MsgKeyboard.MSG_INPUT_KEY.format(key, xpath))
        else:
            self.log.warning(MsgKeyboard.MSG_INPUT_KEY_ERROR)
            
    def combine_keys(self, xpath, key_list):
        """
        Method to enter a combination of keys in a element
        :param xpath: String. Xpath of element
        :param key_list: list. list of name of keys
        """
        keys = ''
        for i in key_list:
            key = self.obtain_key(i)
            keys += key
        self.search_element_by_xpath(xpath).send_keys(keys)
        self.log.info(MsgKeyboard.MSG_INPUT.format(keys, xpath))
            
    def obtain_key(self, key):
        """
        Method to search a key object by string
        :param key: String. Name of key to use
        """
        key = key.lower()
        if key == 'enter': return Keys.ENTER
        elif key == 'alt': return Keys.ALT
        elif key == 'backspace': return Keys.BACKSPACE
        elif key == 'control': return Keys.CONTROL
        elif key == 'delete': return Keys.DELETE
        elif key == 'escape': return Keys.ESCAPE
        elif key == 'shift': return Keys.SHIFT
        elif key == 'space': return Keys.SPACE
        elif key == 'tab': return Keys.TAB
        elif key == 'end': return Keys.END
        elif key == 'home': return Keys.HOME
        elif key == 'page_down': return Keys.PAGE_DOWN
        elif key == 'page_up': return Keys.PAGE_UP
        elif key == 'up': return Keys.UP
        elif key == 'down': return Keys.DOWN
        elif key == 'left': return Keys.LEFT
        elif key == 'right': return Keys.RIGHT
        elif key == 'f1': return Keys.F1
        elif key == 'f2': return Keys.F2
        elif key == 'f3': return Keys.F3
        elif key == 'f4': return Keys.F4
        elif key == 'f5': return Keys.F5
        elif key == 'f6': return Keys.F6
        elif key == 'f7': return Keys.F7
        elif key == 'f8': return Keys.F8
        elif key == 'f9': return Keys.F9
        elif key == 'f10': return Keys.F10
        elif key == 'f11': return Keys.F11
        elif key == 'f12': return Keys.F12
        else: return key
    
    def write(self, xpath, text, to):
        """
        Method to write a text in a input.
        :param xpath: String. Xpath of the searched element.
        :param text: String/Integer. Text to input
        :param to: Integer. Timeout
        """
        if self.visibility_element(xpath, to):
            self.clear(xpath)      
            self.search_element_by_xpath(xpath).send_keys(text)
            self.visibility_element(xpath, to)
            self.log.info(MsgKeyboard.MSG_INPUT.format(xpath, text))
            return True
        else:
            return False
    
    def clear(self, xpath):
        """
        Method to clear an input or a textarea
        :param xpath: String. Xpath of the element
        """
        try:
            self.search_element_by_xpath(xpath).clear()
            self.log.info(MsgKeyboard.MSG_CLEAR)
        except InvalidElementStateException as e:
            self.log.error(MsgKeyboard.MSG_CLEAR_ERROR.format(e, xpath))
            
            
