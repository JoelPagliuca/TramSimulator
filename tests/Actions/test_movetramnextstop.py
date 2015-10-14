'''
Created on 08/10/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Actions.MoveTramNextStop import MoveTramNextStop

class TestMoveTramNextStop(TramSimTest):
    
    def setUp(self):
        TramSimTest.setUp(self)
        self.entitymanager.placeEntity(self.tram, 1, 2) # stop 2

    def test_canDo(self):
        mtns = MoveTramNextStop(self.tram)
        self.assertTrue(mtns.canDo())
        mtns = MoveTramNextStop(self.entity)
        self.assertFalse(mtns.canDo())
    
    def test_do(self):
        mtns = MoveTramNextStop(self.tram)
        mtns.do()
        new_loc = self.entitymanager.whereIs(self.tram)
        self.assertEqual(new_loc, self.stop3)

if __name__ == "__main__":
    unittest.main()