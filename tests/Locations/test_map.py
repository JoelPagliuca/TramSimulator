'''
Created on 11/03/2015

@author: Joel Pagliuca
'''
import unittest

from TramSim.Locations import Map, Location


class TestMap(unittest.TestCase):
    
    def setUp(self):
        self.map_ = Map('Test Map', 3, 4)

    def test_constructor(self):
        self.assertEqual(len(self.map_.grid[0]), 3)
        self.assertEqual(len(self.map_.grid), 4)
    
    def test_addLocation(self):
        self.assertRaises(ValueError, self.map_.addLocation, *[2,2,2])
        self.assertRaises(IndexError, self.map_.addLocation, *[Location('Garbage'), 6, 6])

if __name__ == "__main__":
    unittest.main()