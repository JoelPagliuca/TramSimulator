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
        self.setLocation(self.tram.getStop())
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
    
    def setLocation(self, l):
        '''
        @param l: Location
        '''
        self.location = l
    
    def addAction(self, action):
        '''
        @param action: Action
        '''
        self.actions.append(action)
    
    def description(self):
        '''
        a short description of the Person
        
        @rtype: str
        '''
        loc = self.location
        if loc:
            loc = loc.getName()
        output = "{0} - seat: {1}, location: {2}".format(self.name, self.seat, loc)
        return output
            
########## Tests ##########

def test_tramFunctionality():
    from TramSim.Entities import Tram, Loop
    from TramSim.Locations import Stop
    print("##### TRAM FUNCTIONALITY #####")
    s1 = Stop('Nigeria')
    s2 = Stop('Serbja')
    l = Loop('test loop')
    l.addStop(s1)
    l.addStop(s2)    
    t = Tram(l, s1)
    p = Person('Test Person')
    p.setLocation(s1)
    print(p.description())
    
    print("##### BOARDING AND LEAVING")
    t.openDoors()
    p.boardTram(t)
    print("BOARDING")
    print(p.description())
    print(t)
    p.leaveTram()
    print("LEAVING")
    print(p.description())
    print(t)
    
    print("##### MOVING")
    p.boardTram(t)
    t.closeDoors()
    t.nextStop()
    t.openDoors()
    p.leaveTram()
    print(p.description())

def tests():
    test_tramFunctionality()
    print("##### DONE #####")

########## ##### ##########

if __name__ == '__main__':
    tests()