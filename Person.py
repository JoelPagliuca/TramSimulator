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
        station - the station the person is at
    
    METHODS:
        __init__
        __bool__
        __str__
        boardTram
    
    '''


    def __init__(self, name = 'Person'):
        '''
        Constructor
        '''
        self.name = name
        self.tram = None
        self.station = None
        self. seat = None
    
    ########## GET METHODS ##########
    
    def getName(self):
        '''
        returns the name
        '''
        return self.name
    
    ########## ##### ##########
    
    ########## OVERLOADS ##########
    
    def __str__(self):
        '''
        '''
        return "O"
        
    __repr__ = __str__
    
    def __bool__(self):
        '''
        '''
        return True
    
    ########## ##### ##########
    
    ########## METHODS ##########

    def boardTram(self, tram):
        '''
        puts the person on the tram
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