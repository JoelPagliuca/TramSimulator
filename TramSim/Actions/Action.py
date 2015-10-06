'''
Created on 16/03/2015

@author: Joel Pagliuca
'''

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
        
        TODO: type check
        @param entity: Entity
        '''
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