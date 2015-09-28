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
    
    def getUserChoice(self):
        '''
        gets the user input and chooses from a list
        
        @rtype: Action
        @return: the Action the user chose
        TODO: obvious input handling
        '''
        choices = self.getUserActions()
        if not choices:
            return
        i = 1
        for c in choices:
            print("[{}] {}".format(str(i), c.getDescription()))
            i += 1
        result = int(input("Selection: "))
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