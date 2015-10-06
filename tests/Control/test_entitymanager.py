'''
Created on 16/03/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest


class TestEntityManager(TramSimTest):

    def test_moveEntity(self):
        loc = self.entitymanager.getMap().getLocation(1, 1)
        loc.addEntity(self.entity)
        self.entitymanager.moveEntity(self.entity, 1, 0)
        self.assertFalse(loc.contains(self.entity))
        loc = self.entitymanager.getMap().getLocation(1, 0)
        self.assertTrue(loc.contains(self.entity))

if __name__ == "__main__":
    unittest.main()