'''
Created on 28 Sep 2015

@author: owner
'''

class Spawner(object):
    '''
    Creates clones of certain entities
    '''


    def __init__(self, cloneable):
        '''
        TODO: type checking, or check if has clone()
        @param cloneable: Entity with clone method
        '''
        self.prototype = cloneable
    
    def spawn(self):
        '''
        clone the Entity
        
        @rtype: Entity (same type as cloneable)
        '''
        return self.prototype.clone()