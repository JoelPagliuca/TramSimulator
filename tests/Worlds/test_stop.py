'''
Created on 11/03/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestStop(TramSimTest):

    def test_setTram(self):
        self.stop1.setTram(self.tram)
        self.assertEqual(self.tram, self.stop1.tram)

if __name__ == "__main__":
    unittest.main()