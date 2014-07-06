'''
Created on 08/03/2014

@author: Joel
'''

class Tram:
    '''
    Tram
    
    representation of a tram
    
    PROPERTIES:
        seats - list - contains the passengers
        doorStatus - boolean - True if doors are closed
        loop - the loop the train is on
        TODO: currentStop - the numeric value of the station
    
    METHODS:
        __init__
        __bool__
        __str__
        doorsOpen
        openDoors
        closeDoors
        nextStation
        getNextSeat
    
    '''
    CAPACITY = 128


    def __init__(self, loop, stop):
        '''
        Constructor
        '''
        self.seats = ['#']*self.CAPACITY
        
        self.doorStatus = True
        
        self.loop = loop
        self.currentStop = stop
    
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
    
    def getCurrentStation(self):
        '''
        current station as string
        
        @return: string - name of station
        '''
        return self.loop[self.currentStop]
    
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
        return bool(self.getNextSeat())
    
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
    
    def nextStation(self):
        '''
        changes the station the tram is at
        '''
        self.currentStop = (self.currentStop + 1) % len(self.loop)
    
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
    
    ########## ##### ##########

if __name__ == '__main__':
    pass