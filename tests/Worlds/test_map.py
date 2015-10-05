'''
Created on 11/03/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

from TramSim.Locations import Location


class TestMap(TramSimTest):

    def test_constructor(self):
        self.assertEqual(len(self.map_._grid[0]), 3)
        self.assertEqual(len(self.map_._grid), 4)
    
    def test_addLocation(self):
        self.assertRaises(ValueError, self.map_.addLocation, *[2,2,2])
        self.assertRaises(IndexError, self.map_.addLocation, *[Location('Garbage'), 6, 6])

if __name__ == "__main__":
    unittest.main()