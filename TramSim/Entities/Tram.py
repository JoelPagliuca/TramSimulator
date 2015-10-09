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
        doorStatus - boolean - True if doors are closed
    '''
    CAPACITY = 128


    def __init__(self, name, loop):
        '''
        Constructor
        
        @param loop: TramSim.Worlds.Loop
        '''
        super().__init__(name)
        self.loop = loop
        self.seats = ['#']*self.CAPACITY
        self.doorStatus = True
    
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
    
    
#     def getNextSeat(self):
#         '''
#         returns the index of the next available seat
#         
#         @return: number of seat, None if no available seat
#         '''
#         try:
#             seat = self.seats.index('#') #returns the index of the first '#'
#             return seat
#         except:
#             return None
    
#     def hasAvailableSeat(self):
#         '''
#         @rtype: boolean
#         '''
#         return not self.getNextSeat() is None
#     
#     def isTakingPassengers(self):
#         '''
#         checks if passengers can be taken
#         '''
#         return self.hasAvailableSeat() and self.doorsOpen()
#     
#     def doorsOpen(self):
#         '''
#         '''
#         return not self.doorStatus
#     
#     def openDoors(self):
#         '''
#         opens the doors of the tram
#         '''
#         self.doorStatus = False
#     
#     def closeDoors(self):
#         '''
#         closes the doors
#         '''
#         self.doorStatus = True
#     
#     def seatPassenger(self, passenger, seat):
#         '''
#         puts the passenger in the seat
#         
#         @param passenger: Person
#         @param seat: integer - the seat number
#         '''
#         self.seats[seat] = passenger
#     
#     def clearSeat(self, seat):
#         '''
#         empties the seat
#         
#         @param seat: int
#         '''
#         self.seats[seat] = '#'