'''
Created on 15/10/2015

@author: joel
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Actions.LeaveTram import LeaveTram
from TramSim.Entities.Tram import Tram

class TestLeaveTram(TramSimTest):
    
    def setUp(self):
        TramSimTest.setUp(self)
        self.person1.tram = self.tram
        self.tram.seatPassenger(self.person1, self.tram.getNextSeat())

    def test_canDo(self):
        lt = LeaveTram(self.person1)
        self.tram.openDoors()
        self.assertTrue(lt.canDo())
    
    def test_cantDo(self):
        lt = LeaveTram(self.person2)
        self.person2.tram = Tram(self.loop, "new tram")
        self.assertFalse(lt.canDo())
        lt = LeaveTram(self.person1)
        self.tram.closeDoors()
        self.assertFalse(lt.canDo())
    
    def test_do(self):
        lt = LeaveTram(self.person1)
        lt.do()
        self.assertIsNone(self.person1.tram)
        self.assertNotIn(self.person1, self.tram.getPassengers())
    
    def test_description(self):
        lt = LeaveTram(self.person1)
        self.assertIsInstance(lt.getDescription(), str)

if __name__ == "__main__":
    unittest.main()