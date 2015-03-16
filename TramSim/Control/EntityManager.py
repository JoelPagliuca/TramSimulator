'''
Created on 16/03/2015

@author: Joel Pagliuca
'''

class EntityManager:
    '''
    Will be controlling most of the Entities
    
    PROPERTIES
        _interface: Interfaces.UserInterface - will be rendering information
        _map: Locations.Map - the map for the game
    '''


    def __init__(self, interface, map_):
        '''
        Constructor
        '''
        self._interface = interface
        self._map = map_