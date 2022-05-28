import unittest
import string

class testCases(unittest.TestCase): 
    def testconvertString(self):
        actual = string.convertString("3053", "L")
        assert "3053" == actual
        actual = string.convertString("Beyene", "U")
        assert "BEYENE" == actual
        actual = string.convertString("Thomas Beyene", "U")
        assert "THOMAS BEYENE" == actual
        actual = string.convertString("Interstellar", "L")
        assert "interstellar" == actual
        actual = string.convertString("Interstellar", "O")
        assert "String cannot be converted" == actual

