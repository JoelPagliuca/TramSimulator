'''
Created on 08/03/2014

@author: Joel
'''
import unittest

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
        getStop
        getNextSeat
        hasAvailableSeat
    
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
        self.stop = self.loop.nextStop(self.stop)
    
    def seatPassenger(self, passenger, seat):
        '''
        puts the passenger in the seat
        
        @param passenger: Person
        @param seat: integer - the seat number
        '''
        self.seats[seat] = passenger
    
    def clearSeat(self, seat):
        '''
        empties the seat
        
        @param seat: int
        '''
        self.seats[seat] = '#'
    
########## Tests ##########

class TestTramFunctionality(unittest.TestCase):
    
    def setUp(self):
        self.loop = Loop("Test loop")
        s1 = Stop('Nigeria')
        s2 = Stop('Serbia')
        self.loop.addStop(s1)
        self.loop.addStop(s2)
        self.tram = Tram(self.loop, s1)
    
    def test_simpleFunctions(self):
        # getStop getNextSeat
        self.assertEqual(self.tram.getStop().getName(), 'Nigeria')
        self.assertEqual(self.tram.getNextSeat(), 0)
    
    def test_hasAvailableSeat(self):
        self.assertTrue(self.tram.hasAvailableSeat())
        # simulate a full tram
        self.tram.seats = ['O', 'O']
        self.assertFalse(self.tram.hasAvailableSeat())
    
    def test_doorFunctionality(self):
        self.tram.openDoors()
        self.assertTrue(self.tram.doorsOpen())
        self.tram.closeDoors()
        self.assertFalse(self.tram.doorsOpen())
    
    def test_nextStop(self):
        self.assertEqual(self.tram.stop, self.loop.getStops()[0])
        self.tram.nextStop()
        self.assertEqual(self.tram.stop, self.loop.getStops()[1])
        self.tram.nextStop()
        self.assertEqual(self.tram.stop, self.loop.getStops()[0])

########## ##### ##########

if __name__ == '__main__':
    unittest.main()