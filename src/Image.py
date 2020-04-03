import allure
import time
# import requests
from datetime import datetime
from io import BytesIO
from os.path import join
# from PIL import Image
from base64 import b64decode
from src.utils.constants.english_message import MsgImage
from src.utils.constants.constants import PNG_FILE


class Image():

    def screenshot(self):
        """
        Method to screenshot
        :parm path:Stirng. Path
        :parm filename: String. filename
        """
        # path = str(self.path)
        ext = '.png'
        name = self.path + self.gen_id() + ext
        self.driver.save_screenshot(name)
        self.screenshot_allure()
        self.log.info(MsgImage.MSG_SCREENSHOT.format(name))

    def screenshot_allure(self):
        """
        Method to Allure screenshot
        """
        allure.attach(self.driver.get_screenshot_as_png(), name='screenshot',
                      attachment_type=allure.attachment_type.PNG)
        self.log.info(MsgImage.MSG_ALLURE)


    def gen_id(self):
        """
        Method to generate Id
        :return:
        """
        id = datetime.today().strftime('%Y%m%d%H%M%S')
        return id

    # def get_image(self, xpath, filename):
    #     """
    #     Method to obtain an image from web, searched by xpath
    #     :param xpath: String. Xpath of the element
    #     :param filename: String. Filename of the image
    #     """
    #     if self.visibility_element(xpath, 10):
    #         tag_name = self.get_tag_name(xpath)
    #         if tag_name == 'img' or tag_name == 'canvas':
    #             source = self.get_attribute(xpath, 'src')
    #         else:
    #             self.log.error(MsgImage.MSG_GET_IMAGE_ERROR.format(xpath))
    #     else:
    #         return False
    #
    #     # If the image is in base 64
    #     if 'base64' in source:
    #         base = source.split(',')[1]
    #         source = b64decode(base)
    #     else: # if de source is an url
    #         image = requests.get(source)
    #         source = image.content
    #     with open(filename, 'wb') as file:
    #         file.write(source)
    #     image = Image.open(filename)
    #     self.log.info(MsgImage.MSG_GET_IMAGE.format(xpath, filename))
    #     return image
    #
    def element_screenshoot(self, xpath):
        """
        Method to obtain a screenshot of the searched element
        :param xpath: String. Xpath of the searched element
        :return: Image. Image object of the searched element
        """
#         Esto probar con python3
#         elem = self.search_element_by_xpath(xpath)
#         source = elem.screenshot_as_base64()
#         image = Image.open(BytesIO(b64decode(source)))
#         return image

        # Este metodo no funciona si:
        #        - El elemento se encuentra fuera de los pixeles que puede 
        #          mostrar el monitor (si se usa el scroll)
        #        - El elemento es mas grande que los pixeles que puede mostrar 
        #          el monitor
        pantalla = self.buffer_screenshoot()
        x, y =self.get_location(xpath)
        height, width = self.get_size(xpath)
        left = x
        top = y
        right = x + width
        bottom = y + height
        box = (left, top, right, bottom)
        im = pantalla.crop(box)
        return im
        
    def buffer_screenshoot(self):
        """
        Method to create an image element of screenshot. This image is in 
        buffer.
        :return: Image. Screenshot
        """
        source = self.driver.get_screenshot_as_base64()
        image = Image.open(BytesIO(b64decode(source)))
        self.log.info(MsgImage.MSG_SCREENSHOT_BUFFER)
        return image
        
        
            
        
