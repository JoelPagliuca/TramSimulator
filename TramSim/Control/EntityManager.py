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
    
    def placeEntity(self, entity, x, y):
        '''
        places the entity on the given coordinate
        
        @raise Exception: if coordinates are bad
        '''
        loc = self._map.getLocation(x, y)
        loc.addEntity(entity)
    
    def moveEntity(self, entity, x, y):
        '''
        moves the entity to the given coordinate
        
        @raise Exception: if coordinates are bad, or 
        '''
        loc = self.whereIs(entity)
        loc.removeEntity(entity)
        self.placeEntity(entity, x, y)
        
    
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
    
    def getUserChoice(self):
        '''
        gets the user input and chooses from a list
        
        @rtype: Action
        @return: the Action the user chose
        '''
        choices = self.getUserActions()
        if not choices:
            return
        i = 1
        for c in choices:
            print("[{}] {}".format(str(i), c.getDescription()))
            i += 1
        while True:
            result = input("Selection: ")
            try:
                result = int(result)
            except ValueError:
                continue
            if (result > 0 and result < i):
                break
        return choices[result-1]
    
    def getAIActions(self):
        '''
        gets one action per AI
        
        @rtype: list
        '''
        actions = []
        for e in self.getAllEntities():
            action = e.getAIAction()
            if action:
                actions.append(action)
        return actions
    
    def getMap(self):
        '''
        @rtype: Map
        '''
        return self._map