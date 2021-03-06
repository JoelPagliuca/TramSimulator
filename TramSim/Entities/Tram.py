'''
Created on 08/03/2014

@author: Joel Pagliuca
'''
from TramSim.Entities import Entity

class Tram(Entity):
    '''
    Tram
    
    representation of a tram
    
    PROPERTIES:
        _seats - list - contains the passengers
        _seating - dict - Person -> Seat
        _doorStatus - boolean - True if doors are closed
    '''
    CAPACITY = 128


    def __init__(self, name, loop):
        '''
        Constructor
        
        @param loop: TramSim.Worlds.Loop
        '''
        super().__init__(name)
        self.loop = loop
        self._seats = ['#']*self.CAPACITY
        self._seating = {}
        self._doorStatus = True
    
#     def __str__(self):
#         '''
#         '''
#         if self.doorsOpen():
#             doors = " "
#         else:
#             doors = "-"
#         
#         output = """  //================================={doors}{doors}{doors}=====================================\\\\  
#  //   |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|   \\\\ 
# ||    |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|    ||
# |                                                                               |
# ||    |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|    ||
#  \\\\   |{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{}     {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|{} {}|   // 
#   \\\\================================={doors}{doors}{doors}=====================================//  """.format(*self.seats,doors = doors)
#         return output
    
    
    def getNextSeat(self):
        '''
        returns the index of the next available seat
         
        @return: number of seat, None if no available seat
        '''
        try:
            seat = self._seats.index('#') #returns the index of the first '#'
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
     
    def doorsOpen(self):
        '''
        '''
        return not self._doorStatus
     
    def openDoors(self):
        '''
        opens the doors of the tram
        '''
        self._doorStatus = False
     
    def closeDoors(self):
        '''
        closes the doors
        '''
        self._doorStatus = True
     
    def seatPassenger(self, passenger, seat):
        '''
        puts the passenger in the seat
         
        @param passenger: Person
        @param seat: integer - the seat number
        '''
        self._seats[seat] = passenger
        self._seating[passenger] = seat
    
    def whereIs(self, passenger):
        '''
        finds seat of the passenger
        
        @rtype: int
        @raise ValueError: passenger not in the tram
        '''
        if passenger not in self.getPassengers():
            raise ValueError("Tram.whereIs: passenger not in tram")
        return self._seating[passenger]
     
    def clearSeat(self, seat):
        '''
        empties the seat
        removes the person
         
        @param seat: int
        '''
        passenger = self._seats[seat]
        if passenger in self.getPassengers():
            del self._seating[passenger]
        self._seats[seat] = '#'
    
    def getPassengers(self):
        '''
        @rtype: list <Person>
        '''
        return self._seating.keys()
    
    def getDescription(self):
        '''
        just adds a note about the number of passengers
        '''
        d = super().getDescription()
        num = len(self.getPassengers())
        return d+" with {} passengers".format(num)