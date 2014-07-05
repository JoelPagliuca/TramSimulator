'''
Created on 08/03/2014

@author: Joel
'''

import unittest
from Tram import Tram

class Person:
    '''
    Person
    
    representation of a person
    
    PROPERTIES:
        name - the name of the person
        tram - the tram the person is on
        seat - the seat the person is sitting on
        location - either the stop of the tram or a Location
    
    METHODS:
        __init__
        boardTram
        leaveTram
    
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
        
    def getName(self):
        '''
        returns the name
        '''
        return self.name
    
    def __str__(self):
        '''
        '''
        return "O"
        
    __repr__ = __str__
    
    def __bool__(self):
        '''
        '''
        return True
    
    def boardTram(self, tram):
        '''
        puts the person on the tram
        
        @param tram: Tram
        @precondition: 1 tram must be a Tram
                       2 tram must have open doors
                       3 tram must have at least 1 available seat
        '''
        ermsg = '{} could not board tram'.format(self.name)
        if tram.doorsOpen():
            seat = tram.getNextSeat()
            
            if seat:
                self.tram = tram
                self.seat = seat
                self.tram.seatPassenger(self, self.seat)
            else:
                print(ermsg)
        else:
            print(ermsg)
    
    def leaveTram(self):
        '''
        '''
        if self.tram and self.tram.doorsOpen():
            self.tram.clearSeat(self.seat)
            self.tram = None
            self.seat = None
        else:
            print('Could not leave tram')
    
    ########## ##### ##########

########## TESTS ##########

class TestClassStudentValid(unittest.TestCase):
    '''
    '''
    
    def setUp(self):
        self.person1 = Person("Nigga")
    
    def test_getMethods(self):
        '''
        test the get methods
        '''
        self.assertEqual(self.person1.getName(), "Nigga")

########## ##### ##########

if __name__ == '__main__':
    unittest.main()