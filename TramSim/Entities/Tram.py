'''
Created on 08/03/2014

@author: Joel
'''
from TramSim.Entities import Loop, Person
from TramSim.Locations import Stop

class Tram:
    '''
    Tram
    
    representation of a tram
    
    PROPERTIES:
        seats - list - contains the passengers
        doorStatus - boolean - True if doors are closed
        loop - the loop the train is on
        stop - the stop the tram is currently at
    
    METHODS:
        doorsOpen
        openDoors
        closeDoors
        nextStop
        getNextSeat
    
    OVERLOADS:
        __bool__
        __str__
    
    '''
    CAPACITY = 128


    def __init__(self, loop, stop):
        ''' TODO: stop has to be on loop
        Constructor
        
        @param loop: Loop
        @param stop: Stop
        '''
        self.seats = ['#']*self.CAPACITY
        
        self.doorStatus = True
        
        self.loop = loop
        self.stop = stop
        self.stop.setTram(self)
    
    ########## OVERLOADS ##########
    
    def __str__(self):
        '''
        '''
        if self.doorsOpen():
            doors = " "
        else:
            doors = "-"
        
        output = """  //================================={doors}{doors}{doors}=====================================\\\\  
 //   |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|   \\\\ 
||    |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|    ||
|                                                                               |
||    |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|    ||
 \\\\   |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|   // 
  \\\\================================={doors}{doors}{doors}=====================================//  """.format(*self.seats,doors = doors)
        return output
        
    def __bool__(self):
        '''
        '''
        return True
    
    ########## ##### ##########
    
    ########## QUERIES ##########
    
    def getStop(self):
        '''
        @return: current stop
        @rtype: Stop
        '''
        return self.stop
    
    def getNextSeat(self):
        '''
        returns the index of the next available seat
        
        @return: number of seat, None if no available seat
        '''
        try:
            seat = self.seats.index('#') #returns the index of the first '#'
            return seat
        except:
            return None
    
    def hasAvailableSeat(self):
        '''
        @rtype: boolean
        '''
        return not self.getNextSeat() is None
    
    def isTakingPassengers(self):
        '''
        checks if passengers can be taken
        '''
        return self.hasAvailableSeat() and self.doorsOpen()
    
    ########## ##### ##########
    
    ########## METHODS ##########
    
    def doorsOpen(self):
        '''
        '''
        return not self.doorStatus
    
    def openDoors(self):
        '''
        opens the doors of the tram
        '''
        self.doorStatus = False
    
    def closeDoors(self):
        '''
        closes the doors
        '''
        self.doorStatus = True
    
    def nextStop(self):
        '''
        changes the station the tram is at
        '''
        self.stop = self.loop.getNextStop(self.stop)
    
    def seatPassenger(self, passenger, seat):
        '''
        puts the passenger in the seat
        
        @param passenger: the passenger
        @param seat: integer - the seat number
        '''
        self.seats[seat] = passenger
    
    def clearSeat(self, seat):
        '''
        empties the seat
        
        @param seat: integer - seat number
        '''
        self.seats[seat] = '#'
    
########## Tests ##########

def makeTestTram():
    l = Loop("Test loop")
    s1 = Stop('Nigeria')
    s2 = Stop('Serbia')
    l.addStop(s1)
    l.addStop(s2)
    tram = Tram(l, s1)
    return tram

def test_1():
    print("##### SIMPLE TESTS #####")
    tram = makeTestTram()
    print("stop:", tram.getStop().getName())
    print("next seat:", tram.getNextSeat())

def test_hasAvailableSeat():
    print("##### HASAVAILABLESEAT #####")
    tram = makeTestTram()
    print("with available seat:", tram.hasAvailableSeat())
    tram.seats = ['O', 'O']
    print("without available seat:", tram.hasAvailableSeat())

def test_isTakingPassengers():
    print("##### HASAVAILABLESEAT #####")
    tram = makeTestTram()
    tram.openDoors()
    print("seat, no doors:", tram.isTakingPassengers())
    tram.closeDoors()
    print("seat, doors:", tram.isTakingPassengers())
    tram.openDoors()
    tram.seats = []
    print("no seat, no doors:", tram.isTakingPassengers())

def test_nextStop():
    print("##### NEXTSTOP #####")
    tram = makeTestTram()
    print("stop:", tram.getStop().getName())
    tram.nextStop()
    print("next stop:", tram.getStop().getName())

def tests():
    test_1()
    test_hasAvailableSeat()
    test_isTakingPassengers()
    test_nextStop()
    print("##### DONE #####")

########## ##### ##########

if __name__ == '__main__':
    tests()