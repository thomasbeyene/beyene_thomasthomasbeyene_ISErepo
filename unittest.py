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

    def testcontainsNumValues(self):
        actual = string.ContainsNumbericValue("3053")
        assert True == actual
        actual = string.ContainsNumbericValue("Beyene")
        assert False == actual
        actual = string.ContainsNumbericValue("Thomas Beyene")
        assert False == actual
        actual = string.ContainsNumbericValue("Interstellar",)
        assert False == actual

    def testIsValidNum(self):
        actual = string.IsValidNumber("3053")
        assert True == actual
        actual = string.IsValidNumber("Beyene")
        assert False == actual
        actual = string.IsValidNumber("Thomas Beyene")
        assert False == actual
        actual = string.IsValidNumber("Interstellar",)
        assert False == actual

    def testRemoveNum(self):
        actual = string.IsValidNumber("3053")
        assert '' == actual
        actual = string.IsValidNumber("Beyene")
        assert "Beyene" == actual
        actual = string.IsValidNumber("Thomas Beyene")
        assert "Thomas Beyene" == actual
        actual = string.IsValidNumber("Interstellar",)
        assert "Interstellar" == actual

    def testRemoveNumNConvert(self):
        actual = string.RemoveNumericAndConvert("3053", "U")
        assert '' == actual
        actual = string.RemoveNumericAndConvert("Beyene", "L")
        assert "beyene" == actual
        actual = string.RemoveNumericAndConvert("Thomas Beyene", "L")
        assert "thomas beyene" == actual
        actual = string.RemoveNumericAndConvert("Interstellar", "U")
        assert "INTERSTELLAR" == actual

