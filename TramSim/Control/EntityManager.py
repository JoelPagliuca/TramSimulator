'''
Created on 16/03/2015

@author: Joel Pagliuca
'''

class EntityManager:
    '''
    Will be controlling most of the Entities
    
    PROPERTIES
        _map: Worlds.Map - the map for the game
    '''


    def __init__(self, map_):
        '''
        Constructor
        
        @param map_: Worlds.Map
        '''
        self._map = map_
    
    def getAllEntities(self):
        '''
        @rtype: list
        '''
        return self._map.getAllEntities()
    
    def whereIs(self, entity):
        '''
        gives location containing entity
        '''
        return self._map.whereIs(entity)
    
    def getUserActions(self):
        '''
        gets the Actions the user can perform
        
        @rtype: list
        '''
        output = []
        entities = self.getAllEntities()
        for ent in entities:
            output.extend(ent.getPlayerActions())
        return output
    
    def getUserChoice(self, choices):
        '''
        gets the user input and chooses from a list
        
        @param choices: list
        @rtype: int
        @return: the index of the choice
        '''
        i = 1
        for c in choices:
            print("[{}] {}".format(str(i), str(c)))
            i += 1
        result = int(input("Selection: "))
        return result-1