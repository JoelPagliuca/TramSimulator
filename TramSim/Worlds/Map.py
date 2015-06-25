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
    '''


    def __init__(self, name, sizex, sizey):
        '''
        Constructor
        '''        
        self.name = name
        self._grid = []
        self.width = sizex
        self.height = sizey
        
        row = [Location('Garbage')]*sizex
        for _ in range(sizey):
            self._grid.append(row.copy())
    
    def __str__(self):
        '''
        @rtype: str
        '''
        output = ''
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
        '''
        # START TYPE CHECKING
        # loc
        if not isinstance(loc, Location):
            raise ValueError("loc was not Location")
        # END TYPE CHECKING
        self._grid[locy][locx] = loc