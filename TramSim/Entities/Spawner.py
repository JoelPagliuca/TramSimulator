'''
Created on 28 Sep 2015

@author: Joel Pagliuca
'''

class Spawner(object):
    '''
    Creates clones of certain entities
    Prototype pattern
    '''

    def __init__(self, cloneable):
        '''
        @param cloneable: Entity with clone method
        @raise ValueError: if cloneable is not clone()able
        '''
        # START PRECONDITIONS
        if not hasattr(cloneable, 'clone'):
            raise ValueError("Spawner: cloneable did not have method clone()")
        # END PRECONDITINOS
        self._prototype = cloneable
    
    def spawn(self):
        '''
        clone the Entity
        
        @rtype: Entity (same type as cloneable)
        '''
        return self._prototype.clone()