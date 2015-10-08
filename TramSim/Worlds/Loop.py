'''
Created on 09/03/2014

@author: Joel Pagliuca
'''

class Loop:
    '''
    Loop
    
    representation of a tram loop
    
    PROPERTIES:
        name
        _stops
    '''


    def __init__(self, name):
        '''
        Constructor
        
        @param name: str
        '''
        self.name = str(name)
        self._stops = []
    
    def __iter__(self):
        '''
        will all us to iterate over loop with
        for stop in Loop
        '''
        return iter(self._stops)
    
    def addStop(self, stop):
        '''
        @param stop: Stop
        '''
        self._stops.append(stop)
    
    def getStops(self):
        '''
        @rtype: list 
        '''
        return self._stops.copy()
    
    def removeStop(self, stop):
        '''
        @param stop: Stop
        @precondition: 1 the loop must contain stop
        @raise ValueError: 
        '''
        # while stop in self._stops?
        # START PRECONDITIONS
        # 1
        if not stop in self.getStops():
            raise ValueError('the loop must contain stop')
        # END PRECONDITIONS
        self._stops.remove(stop)
    
    def nextStop(self, stop):
        '''
        @param stop: Stop
        @precondition: 1 stop must be in the loop
        @rtype: Stop
        @raise ValueError: if stop not in loop
        '''
        # START PRECONDITIONS
        # 1
        if not stop in self.getStops():
            raise ValueError("stop must be in the loop")
        # END PRECONDITIONS
        stops = self.getStops()
        index = stops.index(stop)
        index = (index + 1) % len(stops)
        return stops[index]
    
    def getName(self):
        return str(self.name)
    
    def getDescription(self):
        '''
        @rtype: str
        '''
        output = self.getName() + ':'
        for stop in self.getStops():
            output += '\n ' + stop.getName()
        return output