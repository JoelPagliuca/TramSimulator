'''
Created on 12/10/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

from TramSim.Worlds import Map
from TramSim.Actions import MovePersonRandom

class TestMovePersonRandom(TramSimTest):

    def test_canDo(self):
        self.entitymanager.placeEntity(self.entity, 2, 3)
        mpr = MovePersonRandom(self.entity)
        self.assertTrue(mpr.canDo())
    
    def test_cantDo(self):
        m = Map("", 1, 1)
        self.entitymanager._map = m
        m.getLocation(0, 0).addEntity(self.entity)
        mpr = MovePersonRandom(self.entity)
        self.assertFalse(mpr.canDo())
    
    def test_do(self):
        self.entitymanager.placeEntity(self.entity, 2, 3)
        loc = self.map_.getLocation(2, 3)
        mpr = MovePersonRandom(self.entity)
        mpr.do()
        nbrs = [l.contains(self.entity) for l in self.map_.getNeighborLocations(loc)]
        self.assertTrue(any(nbrs))
        self.assertFalse(all(nbrs))
    
    def test_description(self):
        # just make sure it doesn't error
        mpr = MovePersonRandom(self.entity)
        _ = mpr.getDescription()

if __name__ == "__main__":
    unittest.main()