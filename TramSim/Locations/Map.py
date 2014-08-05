'''
Created on 01/08/2014

@author: owner
'''
from TramSim.Locations import Location

class Map:
    '''
    classdocs
    
    PROPERTIES:
        name
        grid
    
    METHODS:
        addLocation
    
    OVERLOADS:
        __str__
    '''


    def __init__(self, name, sizex, sizey):
        '''
        Constructor
        '''        
        self.name = name
        self.grid = []
        self.width = sizex
        self.height = sizey
        
        row = [Location('Garbage')]*sizex
        for _ in range(sizey):
            self.grid.append(row.copy())
    
    def __str__(self):
        '''
        @rtype: str
        '''
        output = ''
        sep = ''
        for row in self.grid:
            rowstr = sep + '|'
            for loc in row:
                rowstr += loc.getSymbol()
            output = output + rowstr + '|'
            sep = '\n'
        return output
    
    def addLocation(self, loc, locx, locy):
        '''
        adds a location to the grid at the specified coordinates
        
        @param loc: Location
        @param locx: int
        @param locy: int
        '''
        # START TYPE CHECKING
        # loc
        if not isinstance(loc, Location):
            raise ValueError("loc was not Location")
        # END TYPE CHECKING
        self.grid[locy][locx] = loc

########## Tests ##########

def test_1():
    print("##### TEST_1 #####")
    m = Map('Nigeria', 5, 3)
    print(m)

def test_2():
    print("##### TEST_2 #####")
    m = Map('Nigeria', 5, 3)
    print('adding Serbia')
    l = Location('Serbia')
    l.setSymbol('S')
    m.addLocation(l, 1, 2)
    print(m)

def tests():
    test_1()
    test_2()
    print("##### DONE #####")

########## ##### ##########

if __name__ == '__main__':
    tests()