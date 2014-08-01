'''
Created on 01/08/2014

@author: owner
'''

class Map:
    '''
    classdocs
    
    PROPERTIES:
        name
        grid
    
    METHODS:
        
    
    OVERLOADS:
        __str__
    '''


    def __init__(self, name, sizex, sizey):
        '''
        Constructor
        '''
        from TramSim.Locations import Location
        
        self.name = name
        self.grid = []
        
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

########## Tests ##########

def test_1():
    print("##### TEST_1 #####")
    m = Map('Nigeria', 5, 3)
    print(m)

def tests():
    test_1()
    print("##### DONE #####")

########## ##### ##########

if __name__ == '__main__':
    tests()