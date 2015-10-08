'''
Created on 09/03/2014

@author: Joel
'''
from TramSim.Worlds import Location


class Stop(Location):
    '''
    Stop
    
    representation of a tram stop
    TODO: have something that lets Stop have multiple trams
    
    PROPERTIES:
        
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        super().__init__(name)