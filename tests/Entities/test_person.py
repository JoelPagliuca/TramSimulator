'''
Created on 05/10/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Entities.Person import Person

class TestPerson(TramSimTest):

    def test_str(self):
        self.assertEqual(str(self.person1), "O")
    
    def test_spawn(self):
        clone = self.person1.clone()
        self.assertIsNotNone(clone)
        self.assertIsInstance(clone, Person)

if __name__ == "__main__":
    unittest.main()