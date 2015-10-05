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
    
    def test_addEntity(self):
        self.location.addEntity(56)
        self.assertIn(56, self.location._contents)
    
    def test_removeEntity(self):
        self.location.addEntity(56)
        self.location.removeEntity(56)
        self.assertNotIn(56, self.location._contents)
        
        self.assertRaises(ValueError, self.location.removeEntity, 57)


if __name__ == "__main__":
    unittest.main()