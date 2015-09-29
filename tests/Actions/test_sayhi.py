'''
Created on 29 Sep 2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestSayHi(TramSimTest):

    def test_canDo(self):
        self.assertTrue(self.sayhi.canDo())
    
    def test_getDescription(self):
        self.assertIsInstance(self.sayhi.getDescription(), str)

if __name__ == "__main__":
    unittest.main()