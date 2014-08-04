'''
Created on 06/07/2014

@author: Joel Pagliuca
'''

class Location(object):
    '''
    Location
    
    PROPERTIES:
        name
    
    METHODS:
        getName
    
    OVERRIDES:
        __bool__
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = str(name)
        self.symbol = '-'
    
    def getName(self):
        return self.name
    
    def __bool__(self):
        return True
    
    def getSymbol(self):
        '''
        - marks the spot
        '''
        return self.symbol
    
    def setSymbol(self, s):
        self.symbol = s