'''
Created on 10/03/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestLocation(TramSimTest):

    def test_getSymbol(self):
        self.assertEqual(self.location.symbol, self.location.getSymbol())
    
    def test_setSymbol(self):
        self.location.setSymbol("S")
        self.assertEqual(self.location.symbol, "S")


if __name__ == "__main__":
    unittest.main()