'''
Created on 11/03/2015

@author: Joel Pagliuca
'''
import unittest

from TramSim.Locations import Stop
from TramSim.Entities import Tram

class TestStop(unittest.TestCase):

    def setUp(self):
        self.stop = Stop('Nigeria')
        self.tram = Tram

    def test_setTram(self):
        self.stop.setTram(self.tram)
        self.assertEqual(self.tram, self.stop.tram)

if __name__ == "__main__":
    unittest.main()