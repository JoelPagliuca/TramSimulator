'''
Created on 08/03/2014

@author: Joel
'''

class Person:
    '''
    Person
    
    representation of a person
    
    PROPERTIES:
        name - the name of the person
        tram - the tram the person is on
        seat - the seat the person is sitting on
        location - either the stop of the tram or a Locations
        actions - actions this entity is capable of performing
    
    METHODS:
        boardTram
        leaveTram
        getLocation
    
    OVERLOADS:
        __bool__
        __str__
    '''


    def __init__(self, name = 'Person'):
        '''
        Constructor
        '''
        self.name = name
        self.tram = None
        self.seat = None
        self.location = None
        self.actions = []
        
    def getName(self):
        '''
        returns the name
        '''
        return self.name
    
    def __str__(self):
        '''
        '''
        return "O"
        
    def __bool__(self):
        '''
        '''
        return True
    
    def boardTram(self, tram):
        from TramSim.Entities import Tram
        '''
        puts the person on the tram
        
        @param tram: Tram
        @precondition: 1 tram must be a Tram
                       2 tram must be able to take passengers
        '''
        # START PRECONDITIONS
        # 1
        if not isinstance(tram, Tram):
            raise ValueError("tram must be a Tram")
        # 2
        if not tram.isTakingPassengers():
            raise AttributeError("tram must be able to take passengers")
        # END PRECONDITIONS
        seat = tram.getNextSeat()
        self.tram = tram
        self.seat = seat
        self.tram.seatPassenger(self, self.seat)
    
    def leaveTram(self):
        '''
        @precondition: 1 Person must be in a tram
                       2 tram must have open doors
        '''
        # START PRECONDITIONS
        # 1
        if self.tram == None:
            raise ValueError("Person must have a Tram set")
        # 2
        if not self.tram.doorsOpen():
            raise AttributeError("tram must have open doors")
        # END PRECONDITIONS
        self.tram.clearSeat(self.seat)
        self.tram = None
        self.seat = None
    
    def getLocation(self):
        '''
        either gets the Stop of the tram or the location
        
        @rtype: Location or None
        '''
        if self.tram:
            return self.tram.getCurrentStop()
        else:
            return self.location
    
    def addAction(self, action):
        '''
        @param action: Action
        '''
        self.actions.append(action)
            
########## ##### ##########

if __name__ == '__main__':
    pass