'''
Created on 29 Sep 2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Actions.Action import Action

class TestEntity(TramSimTest):

    def test_getName(self):
        self.assertEqual(self.entity.getName(), self.entity.name)
    
    def test_playerActions(self):
        self.entity.addPlayerAction(self.sayhi)
        self.assertIn(self.sayhi, self.entity.getPlayerActions())
        self.entity.addPlayerAction(self.sayhi)
        self.assertEqual(len(self.entity.getPlayerActions()), 2)
    
    def test_AIActions(self):
        self.entity.addAIAction(self.sayhi)
        self.assertIn(self.sayhi, self.entity.getPossibleAIActions())
        self.entity.addAIAction(self.sayhi)
        self.assertEqual(len(self.entity.getPossibleAIActions()), 2)
        self.assertIsInstance(self.entity.getAIAction(), Action)

if __name__ == "__main__":
    unittest.main()