'''
Created on 05/10/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Entities.Person import Person

class Test(TramSimTest):

    def test_spawnPerson(self):
        clone = self.personSpawner.spawn()
        self.assertIsNotNone(clone)
        self.assertIsInstance(clone, Person)

if __name__ == "__main__":
    unittest.main()