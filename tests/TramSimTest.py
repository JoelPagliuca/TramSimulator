'''
Created on 13/03/2015

@author: Joel Pagliuca
'''
import unittest

from TramSim.Actions import Action
from TramSim.Actions import *
from TramSim.Entities import Entity
from TramSim.Entities import *
from TramSim.Worlds import *
from TramSim.Control.EntityManager import EntityManager

class TramSimTest(unittest.TestCase):
    '''
    Base unittest for TramSim
    will have a really comprehensive setUp that won't need to be repeated
    because there's currently a lot of repetition in setUp()s and imports
    '''
    
    def setUp(self):
        
        ## Worlds
        
        self.location = Location('Serbia')
        
        self.loop = Loop('Test Loop')
         
        self.stop1 = Stop('Nigeria')
        self.stop2 = Stop('Brazil')
        self.stop3 = Stop('Broviet')
         
        self.loop.addStop(self.stop1)
        self.loop.addStop(self.stop2)
        self.loop.addStop(self.stop3)
         
        self.map_ = Map('Test Map', 3, 4)
        self.map_.addLocation(self.stop1, 0, 0)
        self.map_.addLocation(self.stop2, 1, 2)
        self.map_.addLocation(self.stop3, 2, 0)
        
        ## Control
        
        self.entitymanager = EntityManager(self.map_)
        Entity.EntityManager = self.entitymanager
        
        ## Entities
        
        self.entity = Entity('TEST')
        self.person1 = Person('Person1')
        self.person2 = Person('Person2')
        self.personSpawner = Spawner(self.person1)
        self.tram = Tram("Test Tram", self.loop)
        self.tram.openDoors()
        
        ## Actions
        
        self.action = Action(Entity('TEST'))
        self.sayhi = SayHi(Entity('TEST'))