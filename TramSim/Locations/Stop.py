'''
Created on 09/03/2014

@author: Joel
'''
from TramSim.Locations import Location


class Stop(Location):
    '''
    Stop
    
    representation of a tram stop
    
    PROPERTIES:
        tram
    
    METHODS:
        getTram
        setTram
    
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        super().__init__(name)
        self.tram = None
        
    def getTram(self):
        '''
        '''
        return self.tram
    
    def setTram(self, tram):
        '''
        @param tram: Tram
        '''
        self.tram = tram
    
########## Tests ##########

def test_1():
    print("##### TEST_1 #####")
    s = Stop('Nigeria')
    print(s.getName())

def tests():
    test_1()
    print("##### DONE #####")

########## ##### ##########

if __name__ == '__main__':
    tests()