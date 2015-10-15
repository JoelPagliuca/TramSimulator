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
        @param person: Person
        @param tram: Tram
        '''
        self.person = person
        self.tram = tram

    def canDo(self):
        if self.person.tram is None:
            em = self.person.EntityManager
            ploc = em.whereIs(self.person)
            tloc = em.whereIs(self.tram)
            same_loc = (ploc == tloc)
            return same_loc and self.tram.isTakingPassengers()
        else:
            return False

    def do(self):
        '''
        set the person's tram to the tram
        put the person in the tram
        '''
        self.person.tram = self.tram
        seat = self.tram.getNextSeat()
        self.tram.seatPassenger(self.person, seat)

    def getDescription(self):
        return "{} board {}".format(self.person.name, self.tram.name)