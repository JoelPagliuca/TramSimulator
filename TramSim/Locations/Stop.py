'''
Created on 09/03/2014

@author: Joel
'''
from TramSim.Locations import Location
from TramSim.Entities import Tram

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
    
########## ##### ##########

if __name__ == '__main__':
    pass