'''
Created on 16/03/2015

@author: owner
'''

class Action(object):
    '''
    INTERFACE
    
    An action an Entity can do
    '''


    def __init__(self, entity):
        '''
        Constructor
        '''
        self.entity = entity
    
    def canDo(self):
        '''
        assesses whether the entity can perform the action
        
        @rtype: bool
        '''
        raise NotImplementedError()
    
    def do(self):
        raise NotImplementedError()