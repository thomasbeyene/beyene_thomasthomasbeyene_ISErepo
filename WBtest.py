import unittest
import sys
import io
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
