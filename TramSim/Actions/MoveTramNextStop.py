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
        if not isinstance(self.entity, Tram):
            return False
        
        loop = self.entity.loop
        current_stop = self.entitymanager.whereIs(self.entity)
        try:
            _ = loop.nextStop(current_stop)
            return True
        except ValueError:
            return False
    
    def do(self):
        '''
        '''
        loop = self.entity.loop
        current_stop = self.entitymanager.whereIs(self.entity)
        next_stop = loop.nextStop(current_stop)
        coords = self.entitymanager.getMap().findCoordinates(next_stop)
        self.entitymanager.moveEntity(self.entity, *coords)