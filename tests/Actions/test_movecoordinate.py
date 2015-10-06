'''
Created on 06/10/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Actions.MoveCoordinate import MoveCoordinate

class TestMoveCoordinate(TramSimTest):
    
    def setUp(self):
        TramSimTest.setUp(self)
        self.entitymanager.placeEntity(self.entity, 1, 1)

    def testCanDo(self):
        mc = MoveCoordinate(self.entity, 1, 2)
        self.assertTrue(mc.canDo())
    
    def testCantDo(self):
        mc1 = MoveCoordinate(self.person1, 1, 2)
        mc2 = MoveCoordinate(self.entity, 999, 999)
        self.assertFalse(mc1.canDo())
        self.assertFalse(mc2.canDo())
    
    def testDo(self):
        src  = self.entitymanager.getMap().getLocation(1, 1)
        dest = self.entitymanager.getMap().getLocation(1, 2)
        mc = MoveCoordinate(self.entity, 1, 2)
        self.assertFalse(dest.contains(self.entity))
        mc.do()
        self.assertTrue(dest.contains(self.entity))
        self.assertFalse(src.contains(self.entity))

if __name__ == "__main__":
    unittest.main()