import imp
import unittest
import sys
import io
import ModularityConv
from ModularityConv import IsValidNumber, convertString

class WhiteBoxConvertStr(unittest.TestCase):
    def setUp(self):
        self.capOut = convertString

    def testInputUpper(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("Interstellar\nU")
        assert "INTERSTELLAR", True == self.capOut.convertString

    def testInputLower(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("Interstellar\nL")
        assert "interstellar", False == self.capOut.convertString

    def testInputInvalid(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("Interstellar\nO")
        assert "String cannot be converted", False == self.capOut.convertString

class WhiteBoxValidNum(unittest.TestCase):
    def setUp(self):
        self.capOut = IsValidNumber

    def testInputValid(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("3053")
        assert "3053", True == self.capOut.IsValidNumber

    def testInputInvalid(self):
        capOut = io.StringIO()
        sys.stdout = capOut
        sys.stdin = io.StringIO("Interstellar")
        assert "Interstellar", False == self.capOut.IsValidNumber
    
    def tearDown(self):
        self.capOut


if __name__ == '__main__': 
    WhiteBoxValidNum()
    WhiteBoxConvertStr()
