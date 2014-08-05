'''
Created on 04/08/2014

@author: owner
'''
from TramSim.Interfaces import TextInterface
from TramSim.Entities import *
from TramSim.Locations import *

class MainInterface(TextInterface):
    '''
    The main simulation interface
    
    METHODS:
        
    
    OVERRIDES:
        setFunctions
    
    '''
    
    def __init__(self):
        super().__init__()
        self.initializeGame()
    
    # OVERRIDE
    def setFunctions(self):
        '''
        '''
        self.setFunction("exit", self.uiExit)
        self.setFunction("showmap", self.uiShowMap, "Displays the grid")
        self.setFunction("showtram", self.uiShowTram, "Displays the tram")
    
    def uiShowMap(self, args=None):
        '''
        '''
        print(self.GAMEMAP)
        print()
    
    def initializeGame(self):
        '''
        could probably replace with a World class
        '''
        # map
        world = Map('The Simulation', 17, 5)
        self.GAMEMAP = world
        # stops
        s1 = Stop('Nigeria')
        s1.setSymbol('N')
        s2 = Stop('Serbia')
        s2.setSymbol('S')
        s3 = Stop('Brazil')
        s3.setSymbol('B')
        s4 = Stop('Best Korea')
        s4.setSymbol('K')
        s5 = Stop('Russia')
        s5.setSymbol('R')
        # locations
        l1 = Location('Fountain Gate')
        l1.setSymbol('F')
        # loop
        loop = Loop('Simulation loop')
        loop.addStop(s1)
        loop.addStop(s2)
        loop.addStop(s3)
        loop.addStop(s4)
        loop.addStop(s5)
        self.LOOP = loop
        # tram
        self.TRAM = Tram(loop, loop.getStops()[0])
        
        # add locations to the map
        world.addLocation(s1, 1, 1)
        world.addLocation(s2, 7, 1)
        world.addLocation(s3, 11, 2)
        world.addLocation(s4, 8, 4)
        world.addLocation(s5, 4, 3)
        world.addLocation(l1, 12, 1)
    
    def uiShowTram(self, args=None):
        '''
        '''
        print(self.TRAM)
        print()