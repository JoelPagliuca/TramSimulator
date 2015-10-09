'''
Created on 08/10/2015

@author: Joel Pagliuca
'''
from TramSim.Actions import Action
from TramSim.Entities.Tram import Tram

class MoveTramNextStop(Action):
    '''
    Moves the Tram to the next stop
    '''
    
    def canDo(self):
        '''
        Moves only if there exists a next stop
        
        @rtype: bool
        '''
        em = self.entity.EntityManager
        if not isinstance(self.entity, Tram):
            return False
        
        loop = self.entity.loop
        current_stop = em.whereIs(self.entity)
        try:
            _ = loop.nextStop(current_stop)
            return True
        except ValueError:
            return False
    
    def do(self):
        '''
        '''
        em = self.entity.EntityManager
        loop = self.entity.loop
        current_stop = em.whereIs(self.entity)
        next_stop = loop.nextStop(current_stop)
        coords = em.getMap().findCoordinates(next_stop)
        em.moveEntity(self.entity, *coords)
    
    def getDescription(self):
        em = self.entity.EntityManager
        loop = self.entity.loop
        current_stop = em.whereIs(self.entity)
        next_stop = loop.nextStop(current_stop)
        return "Move {} to {}".format(self.entity.name, next_stop.name)