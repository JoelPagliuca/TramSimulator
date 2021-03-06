'''
Created on 01/08/2014

@author: Joel Pagliuca
'''
from TramSim.Worlds import Location

class Map:
    '''
    classdocs
    
    PROPERTIES:
        name
        _grid
        width
        height
    '''


    def __init__(self, name, sizex, sizey):
        '''
        Constructor
        '''        
        self.name = name
        self._grid = []
        self.width = sizex
        self.height = sizey
        
        row = [None for _ in range(sizex)]
        for _ in range(sizey):
            self._grid.append(row.copy())
            
        prototype = Location('Garbage')
        for y in range(sizey):
            for x in range(sizex):
                self._grid[y][x] = prototype.clone()
    
    def __str__(self):
        '''
        @rtype: str
        '''
        output = self.name+'\n'
        sep = ''
        for row in self._grid:
            rowstr = sep + '|'
            for loc in row:
                rowstr += loc.getSymbol()
            output = output + rowstr + '|'
            sep = '\n'
        return output
    
    def addLocation(self, loc, locx, locy):
        '''
        adds a location to the _grid at the specified coordinates
        
        @param loc: Location
        @param locx: int
        @param locy: int
        @raise ValueError: loc not a Location
        '''
        # START TYPE CHECKING
        # loc
        if not isinstance(loc, Location):
            raise ValueError("loc was not Location")
        # END TYPE CHECKING
        self._grid[locy][locx] = loc
    
    def getLocation(self, locx, locy):
        '''
        gets the location given by the coordinates
        
        @param locx: int
        @param locy: int
        @rtype: Location
        '''
        # START PRECONDITIONS
        # 1
        if not (locx < self.width and locx >= 0):
            raise ValueError("locx ({}) must be valid".format(locx))
        # 2
        if not (locy < self.height and locy >= 0):
            raise ValueError("locy ({}) must be valid".format(locy))
        # END PRECONDITIONS
        return self._grid[locy][locx]
    
    def findCoordinates(self, location):
        '''
        gets the coordinates of the location (0 indexed obviously)
        
        @param location: Location
        @rtype: tuple - (locx, locy) coordinates
                or None if could not be found
        '''
        for i in range(self.height):
            for j in range(self.width):
                loc = self.getLocation(j, i)
                if (loc == location):
                    return (j, i)
        return None
    
    def whereIs(self, entity):
        '''
        gives location containing entity
        
        @param entity: Entity
        @rtype: Location
                or None
        '''
        for i in range(self.height):
            for j in range(self.width):
                loc = self.getLocation(j, i)
                if (loc.contains(entity)):
                    return loc
        return None
    
    def getAllEntities(self):
        '''
        @rtype: list
        '''
        entities = []
        for i in range(self.height):
            for j in range(self.width):
                loc = self.getLocation(j, i)
                entities += loc.getContents()
        return entities
    
    def getNeighborLocations(self, loc):
        '''
        gets the surrounding locations to loc
        
        @param loc: Location
        @rtype: list <Location> 
        '''
        results = []
        (x, y) = self.findCoordinates(loc)
        possibilities = [(x-1, y), (x-1, y+1), (x, y+1), (x+1, y+1),
                         (x+1, y), (x+1, y-1), (x, y-1), (x-1, y-1)]
        for c in possibilities:
            try:
                l = self.getLocation(*c)
                results.append(l)
            except:
                # the coordinate was invalid
                pass
        return results