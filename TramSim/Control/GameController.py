'''
Created on 28 Sep 2015

@author: Joel Pagliuca
'''
from TramSim.Worlds import Map
from TramSim.Control import EntityManager, Scheduler
from TramSim.Interfaces import TextInterface

from TramSim.Entities import Person
from TramSim.Actions import SayHi
from TramSim.Worlds.Location import Location

class GameController(object):
    '''
    Essentially the game loop with some additional set up
    '''


    def __init__(self):
        '''
        Constructor
        Will also construct an EntityManager, Scheduler and TextInterface
        '''
        map_ = self._makeMap()
        self.manager = EntityManager(map_)
        self.scheduler = Scheduler()
        self.interface = TextInterface()
    
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
    
    def _makeMap(self):
        '''
        @rtype: Map
        TODO: MapFactory
        '''
        m = Map("Game World", 15, 10)
        l = Location('The Location')
        m.addLocation(l, 6, 6)
        p = Person("The Guy")
        p.addPlayerAction(SayHi(p))
        l.addEntity(p)
        return m