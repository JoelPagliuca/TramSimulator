'''
Created on 09/03/2014

@author: Joel
'''

class Loop:
    '''
    Loop
    
    representation of a tram loop
    
    PROPERTIES:
        stops
    
    METHODS:
        addStop
        getStops
        removeStop
    
    '''


    def __init__(self, name):
        '''
        Constructor
        
        @param name: str
        '''
        self.name = str(name)
        self.stops = []
    
    def addStop(self, stop):
        '''
        @param stop: Stop
        '''
        self.stops.append(stop)
    
    def getStops(self):
        '''
        @rtype: list 
        '''
        return self.stops
    
    def removeStop(self, stop):
        '''
        @param stop: Stop
        @precondition: 1 the loop must contain stop
        @raise ValueError: 
        '''
        # while stop in self.stops?
        # START PRECONDITIONS
        # 1
        if not stop in self.getStops():
            raise ValueError('the loop must contain stop')
        # END PRECONDITIONS
        self.stops.remove(stop)