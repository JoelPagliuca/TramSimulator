'''
Created on 28 Sep 2015

@author: Joel Pagliuca
'''
from TramSim.Entities import Entity
from TramSim.Control import EntityManager, Scheduler
from TramSim import Game

from TramSim.Worlds import MapFactory

class GameController(object):
    '''
    Essentially the game loop with some additional set up
    '''


    def __init__(self):
        '''
        Constructor
        Will also construct an EntityManager, Scheduler and TextInterface
        '''
        mf = MapFactory()
        map_ = mf.citymap()
        self.manager = EntityManager(map_)
        Entity.EntityManager = self.manager
        self.scheduler = Scheduler()
        self.interface = Game.INTERFACE
        self.interface.render(map_)
    
    def loop(self):
        '''
        the game loop
        will block
        '''
        while True:
            # handle user input
            a = self.manager.getUserChoice()
            if a:
                self.scheduler.schedule(a)
            # update
            for a in self.manager.getAIActions():
                self.scheduler.schedule(a)
            self.scheduler.tick()
            # render
            self.interface.render(self.manager.getMap())
            for ent in self.manager.getAllEntities():
                self.interface.render("\n")
                self.interface.render(ent.getDescription())
            self.interface.render("\n")