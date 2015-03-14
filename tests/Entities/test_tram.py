'''
Created on 29/12/2014

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestTramFunctionality(TramSimTest):
    
    def test_simpleFunctions(self):
        # getStop getNextSeat
        self.assertEqual(self.tram.getStop().getName(), 'Nigeria')
        self.assertEqual(self.tram.getNextSeat(), 0)
    
    def test_hasAvailableSeat(self):
        self.assertTrue(self.tram.hasAvailableSeat())
        # simulate a full tram
        self.tram.seats = ['O', 'O']
        self.assertFalse(self.tram.hasAvailableSeat())
    
    def test_doorFunctionality(self):
        self.tram.openDoors()
        self.assertTrue(self.tram.doorsOpen())
        self.tram.closeDoors()
        self.assertFalse(self.tram.doorsOpen())
    
    def test_nextStop(self):
        self.assertEqual(self.tram.stop1, self.loop.getStops()[0])
        self.tram.nextStop()
        self.assertEqual(self.tram.stop1, self.loop.getStops()[1])
        self.tram.nextStop()
        self.assertEqual(self.tram.stop1, self.loop.getStops()[0])

if __name__ == "__main__":
    unittest.main()