import logging
from src.utils.constants.Log_constants import (FORMATTER, FATAL, CRITICAL, ERROR,
                                           WARNING, DEBUG, INFO, NO_VALID)

class Log:
    def __init__(self, path=None, console=True, level=INFO):
        self.__logger = logging.getLogger(__name__)
        self.__formatter = logging.Formatter(FORMATTER)
        self.__logger.setLevel(logging.INFO)
        if path is not None:
            self.__logger_file(path, level)
        if console:
            self.__logger_console(level)
        
    def get_logger(self):
        return self.__logger
    
    def __logger_console(self, level):
        consoleHandler = logging.StreamHandler()
        consoleHandler.setFormatter(self.__formatter)
        consoleHandler.setLevel(self.__get_level(level))
        self.__logger.addHandler(consoleHandler)
    
    def __logger_file(self, path, level):
        handler_info = logging.FileHandler(path)
        handler_info.setLevel(self.__get_level(level))
        handler_info.setFormatter(self.__formatter)
        self.__logger.addHandler(handler_info)
        
    def __get_level(self, level):
        if level.lower() == ERROR:
            return logging.ERROR
        elif level.lower() == CRITICAL:
            return logging.CRITICAL
        elif level.lower() == WARNING:
            return logging.WARNING
        elif level.lower() == FATAL:
            return logging.FATAL
        elif level.lower() == DEBUG:
            return logging.DEBUG
        elif level.lower() == INFO:
            return logging.INFO
        else:
            print(NO_VALID)