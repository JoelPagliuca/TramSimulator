'''
Created on 09/03/2014

@author: Joel
'''
from TramSim.Worlds import Location


class Stop(Location):
    '''
    Stop
    
    representation of a tram stop
    
    PROPERTIES:
        
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        super().__init__(name)