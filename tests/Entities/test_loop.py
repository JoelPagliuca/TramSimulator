'''
Created on 29/12/2014

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestLoopFunctions(TramSimTest):
    
    def test_addStop(self):
        # addStop should add the stop to the list of stops
        self.loop.addStop(self.stop1)
        self.assertEqual(self.loop.stops[-1], self.stop1)
        
        self.loop.addStop(self.stop2)
        self.assertEqual(self.loop.stops[-1], self.stop2)
    
    def test_removeStop(self):
        # removeStop should remove the stop from the list or throw an exception if it isn't there
        self.loop.addStop(self.stop3)
        self.loop.removeStop(self.stop3)
        self.assertTrue(not self.stop3 in self.loop.stops)
        
        self.assertRaises(ValueError, self.loop.removeStop, self.stop3)
    
    def test_nextStop(self):
        self.loop.addStop(self.stop1)
        self.loop.addStop(self.stop2)
        self.assertEqual(self.loop.nextStop(self.stop1), self.stop2)
        self.assertEqual(self.loop.nextStop(self.stop2), self.stop1)

if __name__ == "__main__":
    unittest.main()