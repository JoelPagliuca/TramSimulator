'''
Created on 25/06/2015

@author: Joel Pagliuca
'''
import random

class Entity(object):
    '''
    Entity
    
    PROPERTIES:
        name
        entityManager
        _possibleActions - list of actions that may be randomly selected
        _playerActions - list of actions that a player may select
    '''


    EntityManager = None # should set this before using
    
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self._possibleActions = []
        self._playerActions = []
    
    def addPlayerAction(self, action):
        '''
        @param action: Action
        '''
        self._possibleActions.append(action)
    
    def addPossibleAction(self, action):
        '''
        @param action: Action
        '''
        self._possibleActions.append(action)
    
    def getPlayerActions(self):
        '''
        gets the player actions that can be done
        
        @rtype: List
        '''
        options = []
        for a in self._playerActions:
            if a.canDo():
                options.append(a)
        return options
    
    def getPossibleActions(self):
        '''
        gets the AI actions that can be done
        
        @rtype: List
        '''
        options = []
        for a in self._possibleActions:
            if a.canDo():
                options.append(a)
        return options
    
    def getRandomAction(self):
        '''
        @rtype: Action
        '''
        return random.choice(self.getPossibleActions())