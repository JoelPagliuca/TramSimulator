'''
Created on 05/10/2015

@author: joel
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestPerson(TramSimTest):

    def test_str(self):
        self.assertEqual(str(self.person1), "O")

if __name__ == "__main__":
    unittest.main()