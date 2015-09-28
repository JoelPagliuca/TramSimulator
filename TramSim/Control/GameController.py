'''
Created on 28 Sep 2015

@author: Joel Pagliuca
'''
from TramSim.Worlds import Map
from TramSim.Control import EntityManager, Scheduler
from TramSim.Interfaces import TextInterface

class GameController(object):
    '''
    Essentially the game loop with some additional set up
    '''


    def __init__(self):
        '''
        Constructor
        Will also construct an EntityManager, Scheduler and TextInterface
        '''
        map_ = Map("Game World", 15, 10)
        self.em = EntityManager(map_)
        self.scheduler = Scheduler()
        self.interface = TextInterface()
    
    def loop(self):
        '''
        the game loop
        will block
        '''
        while True:
            # handle user input
            a = self.em.getUserChoice()
            if a:
                self.scheduler.queue_action(a)
            # update
            for a in self.em.getAIActions():
                self.scheduler.queue_action(a)
            self.scheduler.tick()
            # render