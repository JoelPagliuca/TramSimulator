'''
Created on 15/10/2015

@author: Joel Pagliuca
'''
from TramSim.Actions.Action import Action

class BoardTram(Action):
    '''
    Have a Person board a Tram
    '''
    def __init__(self, person, tram):
        '''
        @param entity: Person
        @param tram: Tram
        '''
        self.entity = person
        self.tram = tram

    def canDo(self):
        if self.entity.tram is None:
            em = self.entity.EntityManager
            ploc = em.whereIs(self.entity)
            tloc = em.whereIs(self.tram)
            same_loc = (ploc == tloc)
            return same_loc and self.tram.isTakingPassengers()
        else:
            return False

    def do(self):
        '''
        set the entity's tram to the tram
        put the entity in the tram
        '''
        self.entity.tram = self.tram
        seat = self.tram.getNextSeat()
        self.tram.seatPassenger(self.entity, seat)

    def getDescription(self):
        return "{} board {}".format(self.entity.name, self.tram.name)