'''
Created on 15/10/2015

@author: Joel Pagliuca
'''
from TramSim.Actions.Action import Action

class LeaveTram(Action):
    '''
    Have the person leave the tram
    '''
    
    def __init__(self, person):
        '''
        @param person: Person
        '''
        self.person = person

    def canDo(self):
        '''
        only if the person is on a tram and the doors are open
        
        @rtype: Bool
        '''
        tram = self.person.tram
        conditions = []
        conditions.append(tram is not None)
        conditions.append(tram.doorsOpen())
        conditions.append(self.person in tram.getPassengers())
        return all(conditions)

    def do(self):
        '''
        remove the reference to the tram in person
        take the person off the tram
        '''
        tram = self.person.tram
        seat = tram.whereIs(self.person)
        tram.clearSeat(seat)
        self.person.tram = None

    def getDescription(self):
        return "{} leave {}".format(self.person.name, self.person.tram.name)