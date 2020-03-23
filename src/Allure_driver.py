import allure
from src.utils.constants.english_message import MsgAllure


class Allure_driver():
    def attach_element(self, image, description):
        """
        Method to attach a image in allure
        :param image: Image. Image to attach
        :param description: String. Description of attached image
        """
        allure.attach(image, description, 
                      attachment_type=allure.attachment_type.JPG)
        self.log.info(MsgAllure.MSG_ATTACH_IMAGE.format(description))
    
    def step(self, number, description):
        """
        Method to obtain allure step
        :param number: Integer. Number of step
        :param description: String. Desciption of step
        """
        return allure.step(MsgAllure.MSG_STEP.format(number, description))

