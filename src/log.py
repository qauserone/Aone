import time
import os
from src.utils.Log import Log
from src.utils.constants.My_constants import *
from src.utils.constants.english_message import MsgLog


class log():


    def create_path(self):
        """
        Create the path of test folder. If the folder doesn't exist, it's
        created
        """
        dia = time.strftime("%Y-%m-%d")  # formato aaaa/mm/dd
        hora = time.strftime("%H%M%S")  # formato 24 houras
        TestCase = self.__class__.__name__
        horaAct = hora
        self.path = os.path.join(path_evidence, dia, TestCase, horaAct, '')
        if not os.path.exists(self.path): # si no existe el directorio lo crea
            os.makedirs(self.path)

    def create_log(self):
        """
        Create the log of test. The log is created in the test folder
        """
        self.create_path()
        TestCase = self.__class__.__name__
        # log_path = LOG_PATH.format(self.path, TestCase)
        log_path = self.path + TestCase
        self.log = Log(log_path)
        self.log = self.log.get_logger()
        self.log.info(MsgLog.MSG_CREATE_LOG.format(log_path))
