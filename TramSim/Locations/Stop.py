'''
Created on 09/03/2014

@author: Joel
'''

class Stop:
    '''
    Stop
    
    representation of a tram stop
    
    PROPERTIES:
        
    METHODS:
        
    
    '''


    def __init__(self, name):
        '''
        Constructor
        '''
        self.name = name
        self.tram = None
    
    ########## OVERLOADS ##########
    
    def __bool__(self):
        '''
        '''
        return True
    
    ########## ##### ##########
    
    ########## GET METHODS ##########
    
    def getTram(self):
        '''
        '''
        return self.tram
    
    def setTram(self, tram):
        '''
        '''
        self.tram = tram
    
    ########## ##### ##########
    
    ########## METHODS ##########
    
    
    
    ########## ##### ##########

if __name__ == '__main__':
    pass