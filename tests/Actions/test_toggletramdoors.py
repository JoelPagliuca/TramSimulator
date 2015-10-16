'''
Created on 16/10/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Actions.ToggleTramDoors import ToggleTramDoors

class TestToggleTramDoors(TramSimTest):
    
    def setUp(self):
        TramSimTest.setUp(self)
        self.toggle = ToggleTramDoors(self.tram)
    
    def test_canDo(self):
        self.assertTrue(self.toggle.canDo())
    
    def test_do(self):
        self.tram.openDoors()
        self.toggle.do()
        self.assertFalse(self.tram.doorsOpen())
        self.toggle.do()
        self.assertTrue(self.tram.doorsOpen())
    
    def test_description(self):
        self.assertIsInstance(self.toggle.getDescription(), str)

if __name__ == "__main__":
    unittest.main()