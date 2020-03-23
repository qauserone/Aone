import unittest
from src.Aone import Aone


class MyTestCase(unittest.TestCase):


    def test_openchrome(self):
        a = Aone()
        a.open_browser('file:///home/devuser/Desktop/bkp/html/index.html')
        a.visibility_element('//*[@id="contact"]/h3')
        a.driver.close()

if __name__ == '__main__':
    unittest.main()
