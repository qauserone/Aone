import unittest


class TestPythonTestFail(unittest.TestCase):


    def test_something(self):
        self.assertEqual(True, False)


if __name__ == '__main__':
    unittest.main()
