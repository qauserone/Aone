import pytest


class Errors():


    def fail(self, description):
        """
        Method to show a fail in the test. Attach an image in allure and,
        print in the log the error
        :param description: String. Description of the image.
        """
        self.capture_image(description)
        self.log.error(description)
        pytest.fail(description)
        
    def skip(self, description):
        """
        Method to skip a test. Attach an image in allure and,
        print a warning in the log.
        :param description: String. Description of the image.
        """
        self.capture_image(description)
        self.log.warning(description)
        pytest.skip(description)