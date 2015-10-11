'''
Created on 11/03/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

from TramSim.Worlds import Location


class TestMap(TramSimTest):

    def test_constructor(self):
        self.assertEqual(len(self.map_._grid[0]), 3)
        self.assertEqual(len(self.map_._grid), 4)
    
    def test_addLocation(self):
        self.assertRaises(ValueError, self.map_.addLocation, *[2,2,2])
        self.assertRaises(IndexError, self.map_.addLocation, *[Location('Garbage'), 6, 6])
        self.map_.addLocation(Location('Garbage'), 2, 2)
    
    def test_findCoordinates(self):
        loc = Location("TEST")
        self.map_.addLocation(loc, 2, 2)
        co = self.map_.findCoordinates(loc)
        self.assertTupleEqual(co, (2, 2))
        self.assertIsNone(self.map_.findCoordinates(Location("NOTTEST")))
    
    def test_whereIs(self):
        loc = self.map_.getLocation(2, 2)
        loc.addEntity(self.person1)
        loc2 = self.map_.whereIs(self.person1)
        self.assertEqual(loc, loc2)
    
    
    def test_getAllEntities(self):
        loc = self.map_.getLocation(1, 1)
        loc.addEntity(self.person1)
        loc = self.map_.getLocation(0, 2)
        loc.addEntity(self.person2)
        loc.addEntity(self.entity)
        alle = self.map_.getAllEntities()
        self.assertListEqual(alle, [self.person1, self.person2, self.entity])
        self.assertEqual(3, len(alle))
    
    def test_getNeighborLocations(self):
        loc = self.map_.getLocation(0, 0)
        res = self.map_.getNeighborLocations(loc)
        self.assertEqual(len(res), 3)
        loc = self.map_.getLocation(1, 1)
        res = self.map_.getNeighborLocations(loc)
        self.assertEqual(len(res), 8)

if __name__ == "__main__":
    unittest.main()