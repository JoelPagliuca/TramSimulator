'''
Created on 28 Sep 2015

@author: JoelPagliuca
'''

class GameController(object):
    '''
    Essentially the game loop with some additional set up
    '''


    def __init__(self, entity_manager, scheduler, interface):
        '''
        Constructor
        
        @param entity_manager: EntityManager
        @param scheduler: Scheduler
        '''
        self.em = entity_manager
        self.scheduler = scheduler
        self.interface = interface
    
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