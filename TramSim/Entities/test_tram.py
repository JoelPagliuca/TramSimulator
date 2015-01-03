'''
Created on 29/12/2014

@author: Joel Pagliuca
'''
import unittest

from TramSim.Entities import Loop, Tram
from TramSim.Locations import Stop

class TestTramFunctionality(unittest.TestCase):
    
    def setUp(self):
        self.loop = Loop("Test loop")
        s1 = Stop('Nigeria')
        s2 = Stop('Serbia')
        self.loop.addStop(s1)
        self.loop.addStop(s2)
        self.tram = Tram(self.loop, s1)
    
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
        self.assertEqual(self.tram.stop, self.loop.getStops()[0])
        self.tram.nextStop()
        self.assertEqual(self.tram.stop, self.loop.getStops()[1])
        self.tram.nextStop()
        self.assertEqual(self.tram.stop, self.loop.getStops()[0])

if __name__ == "__main__":
    unittest.main()