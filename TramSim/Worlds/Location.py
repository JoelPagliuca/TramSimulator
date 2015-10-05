'''
Created on 06/07/2014

@author: Joel Pagliuca
'''

class Location(object):
    '''
    Location
    
    PROPERTIES:
        name
        symbol
        _contents
    '''


    def __init__(self, name):
        '''
        Constructor
        
        @param name: str
        '''
        self.name = str(name)
        self.symbol = '-'
        self._contents = []
    
    def getName(self):
        '''
        @rtype: str
        '''
        return self.name
    
    def getSymbol(self):
        '''
        - marks the spot
        @rtype: str
        '''
        return self.symbol
    
    def setSymbol(self, s):
        self.symbol = s
    
    def addEntity(self, ent):
        '''
        adds the entity to the contents of the location
        '''
        self._contents.append(ent)
    
    def contains(self, ent):
        '''
        @rtype: bool
        '''
        return ent in self._contents
    
    def removeEntity(self, ent):
        '''
        removes the entity from the contents
        
        @precondition: ent must be in contents
        @raise ValueError: ent not in contents
        '''
        # START PRECONDITION
        # 1
        if not ent in self._contents:
            raise ValueError("{0} not in {1}".format(str(ent), self.name))
        # END PRECONDITION
        self._contents.remove(ent)
    
    def getContents(self):
        '''
        @rtype: list
        '''
        return self._contents.copy()
    
    def clone(self):
        '''
        @rtype: Location
        '''
        new_location = Location(self.name)
        new_location.setSymbol(self.getSymbol())
        return new_location