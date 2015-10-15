'''
Created on 15/10/2015

@author: Joel Pagliuca
'''
from TramSim.Actions.Action import Action

class LeaveTram(Action):
    '''
    Have the entity leave the tram
    '''
    
    def __init__(self, person):
        '''
        @param entity: Person
        '''
        self.entity = person

    def canDo(self):
        '''
        only if the entity is on a tram and the doors are open
        
        @rtype: Bool
        '''
        if self.entity.tram is None:
            return False
        tram = self.entity.tram
        conditions = []
        conditions.append(tram is not None)
        conditions.append(tram.doorsOpen())
        conditions.append(self.entity in tram.getPassengers())
        return all(conditions)

    def do(self):
        '''
        remove the reference to the tram in entity
        take the entity off the tram
        '''
        tram = self.entity.tram
        seat = tram.whereIs(self.entity)
        tram.clearSeat(seat)
        self.entity.tram = None

    def getDescription(self):
        return "{} leave {}".format(self.entity.name, self.entity.tram.name)