'''
Created on 15/10/2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest
from TramSim.Actions.BoardTram import BoardTram

class TestBoardTram(TramSimTest):

    def test_canDo(self):
        self.entitymanager.placeEntity(self.person1, 1, 1)
        self.entitymanager.placeEntity(self.tram, 1, 1)
        board = BoardTram(self.person1, self.tram)
        self.tram.openDoors()
        self.assertTrue(board.canDo())
    
    def test_cantDo(self):
        self.entitymanager.placeEntity(self.person1, 1, 1)
        self.entitymanager.placeEntity(self.tram, 1, 1)
        board = BoardTram(self.person1, self.tram)
        self.tram.closeDoors()
        self.assertFalse(board.canDo())
        self.tram.openDoors()
        self.entitymanager.moveEntity(self.tram, 2, 2)
        self.assertFalse(board.canDo())
    
    def test_do(self):
        self.entitymanager.placeEntity(self.person1, 1, 1)
        self.entitymanager.placeEntity(self.tram, 1, 1)
        board = BoardTram(self.person1, self.tram)
        self.tram.openDoors()
        board.do()
        self.assertIn(self.person1, self.tram.getPassengers())

if __name__ == "__main__":
    unittest.main()