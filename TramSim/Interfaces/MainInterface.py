'''
Created on 04/08/2014

@author: owner
'''
from TramSim.Interfaces import TextInterface

class MainInterface(TextInterface):
    '''
    The main simulation interface
    
    METHODS:
        
    
    OVERRIDES:
        setFunctions
    
    '''
    
    # OVERRIDE
    def setFunctions(self):
        '''
        '''
        self.setFunction("exit", self.uiExit)