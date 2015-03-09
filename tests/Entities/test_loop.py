'''
Created on 29/12/2014

@author: Joel Pagliuca
'''
import unittest

from TramSim.Entities import Loop
from TramSim.Locations import Stop

class TestLoopFunctions(unittest.TestCase):
    
    def setUp(self):
        self.loop = Loop("Test Loop")
        self.s1 = Stop('Nigeria')
        self.s2 = Stop('Brazil')
    
    def test_addStop(self):
        # addStop should add the stop to the list of stops
        self.loop.addStop(self.s1)
        self.assertEqual(self.loop.stops[-1], self.s1)
        
        self.loop.addStop(self.s2)
        self.assertEqual(self.loop.stops[-1], self.s2)
    
    def test_removeStop(self):
        # removeStop should remove the stop from the list or throw an exception if it isn't there
        self.loop.addStop(self.s1)
        self.loop.removeStop(self.s1)
        self.assertTrue(not self.s1 in self.loop.stops)
        
        self.assertRaises(ValueError, self.loop.removeStop, self.s2)
    
    def test_nextStop(self):
        self.loop.addStop(self.s1)
        self.loop.addStop(self.s2)
        self.assertEqual(self.loop.nextStop(self.s1), self.s2)
        self.assertEqual(self.loop.nextStop(self.s2), self.s1)