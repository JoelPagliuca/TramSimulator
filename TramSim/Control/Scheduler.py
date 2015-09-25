'''
Created on 11/07/2015

@author: JoelPagliuca
'''

class Scheduler(object):
    '''
    Scheduler
    
    Keeps track of some actions, then makes them happen
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self._actions = []
    
    def queue_action(self, action):
        '''
        TODO: better method name
        
        @param action: Action
        '''
        self._actions.append(action)
    
    def tick(self):
        '''
        runs all the queued actions
        '''
        for a in self._actions:
            a.do()