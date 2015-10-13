'''
Created on 29/12/2014

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestTramFunctionality(TramSimTest):
    
    def test_getNextSeat(self):
        seat = self.tram.getNextSeat()
        self.assertEqual(seat, 0)
    
    def test_seatPassenger(self):
        for i in range(10):
            self.tram.seatPassenger(self.personSpawner.spawn(), i)
        self.assertEqual(len(self.tram.getPassengers()), 10)
    
    def test_clearSeat(self):
        for i in range(10):
            self.tram.seatPassenger(self.personSpawner.spawn(), i)
        self.tram.clearSeat(6)
        self.tram.clearSeat(2)
        self.assertEqual(len(self.tram.getPassengers()), 8)

if __name__ == "__main__":
    unittest.main()