'''
Created on 16/03/2015

@author: Joel Pagliuca
'''
from TramSim.Entities import Entity

class Action(object):
    '''
    ABSTRACT
    
    An action an Entity can do
    
    PROPERTIES:
        entity
    '''

    def __init__(self, entity, **kwargs):
        '''
        Constructor
        
        @param entity: Entity
        '''
        # START PRECONDITIONS
        # 1
        if not isinstance(entity, Entity):
            raise ValueError("Action: entity must be an Entity")
        # END PRECONDITIONS
        self.entity = entity
    
    def canDo(self):
        '''
        assesses whether the entity can perform the action
        
        @rtype: bool
        '''
        raise NotImplementedError()
    
    def do(self):
        '''
        perform the action
        '''
        raise NotImplementedError()
    
    def getDescription(self):
        '''
        gets a description of what the action is
        '''
        raise NotImplementedError()