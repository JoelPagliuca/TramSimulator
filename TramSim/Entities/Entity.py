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
        EntityManager
        _AIActions - list of actions that may be randomly selected
        _playerActions - list of actions that a player may select
    '''


    EntityManager = None # should set this before using
    
    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self._AIActions = []
        self._playerActions = []
    
    def getName(self):
        '''
        returns the name
        '''
        return self.name
    
    def addPlayerAction(self, action):
        '''
        @param action: Action
        '''
        self._playerActions.append(action)
    
    def addAIAction(self, action):
        '''
        @param action: Action
        '''
        self._AIActions.append(action)
    
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
    
    def getAllPlayerActions(self):
        '''
        @rtype: list
        '''
        return self._playerActions.copy()
    
    def getPossibleAIActions(self):
        '''
        gets the AI actions that can be done
        
        @rtype: List
        '''
        options = []
        for a in self._AIActions:
            if a.canDo():
                options.append(a)
        return options
    
    def getAIAction(self):
        '''
        a random AI Action
        
        @rtype: Action or None
        '''
        try:
            return random.choice(self.getPossibleAIActions())
        except IndexError:
            return None
    
    def getAllAIActions(self):
        '''
        @rtype: list
        '''
        return self._AIActions.copy()
    
    def update(self):
        '''
        probably for updating the possible actions
        '''
        pass
    
    def getDescription(self):
        '''
        @rtype: str
        '''
        loc = self.EntityManager.whereIs(self)
        if loc:
            coords = self.EntityManager.getMap().findCoordinates(loc)
            d = "{} is at {} ({}, {})".format(self.getName(), loc.getName(), *coords)
        else:
            d = "{} is nowhere to be found".format(self.getName())
        return d
    
    def getEntityManager(self):
        '''
        @rtype: EntityManager
        '''
        return self.EntityManager