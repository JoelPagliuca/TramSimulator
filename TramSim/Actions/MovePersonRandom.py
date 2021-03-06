'''
Created on 12/10/2015

@author: Joel Pagliuca
'''
from random import choice

from TramSim.Actions import Action

class MovePersonRandom(Action):
    '''
    Move a person to a random neighbor location
    '''
    
    def canDo(self):
        '''
        If there's at least 1 option to move to
        
        @rtype: bool
        '''
        em = self.entity.EntityManager
        loc = em.whereIs(self.entity)
        opts = em.getMap().getNeighborLocations(loc)
        not_in_tram = True
        try:
            not_in_tram = not self.entity.tram
        except:
            pass # TODO: yeah this could probably be done better
        return (len(opts) > 0) and not_in_tram
        
    def do(self):
        em = self.entity.EntityManager
        loc = em.whereIs(self.entity)
        opts = em.getMap().getNeighborLocations(loc)
        new_loc = choice(opts)
        em.moveEntity(self.entity, *em.getMap().findCoordinates(new_loc))
    
    def getDescription(self):
        return "Move {} to a neighboring location".format(self.entity.name)