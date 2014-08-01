'''
Created on 09/03/2014

@author: Joel
'''
from TramSim.Locations import Stop

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
    
    def getNextStop(self, stop):
        '''
        @param stop: Stop
        @precondition: 1 stop must be in the loop
        @rtype: Stop
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

########## Tests ##########

def test_1():
    print("##### ADDSTOP #####")
    l = Loop("Test loop")
    def disp(s):
        l.addStop(s)
        print(l.getDescription())
    disp(Stop('Nigeria'))
    disp(Stop('Austria'))
    disp(Stop('Argentina'))

def test_2():
    print("##### REMOVESTOP #####")
    l = Loop("Test loop")
    s = Stop('Nigeria')
    l.addStop(s)
    print(l.getDescription())
    l.removeStop(s)
    print(l.getDescription())

def test_3():
    print("##### NEXTSTOP #####")
    l = Loop("Test loop")
    s1 = Stop('Nigeria')
    s2 = Stop('Austria')
    s3 = Stop('Argentina')
    l.addStop(s1)
    l.addStop(s2)
    l.addStop(s3)
    s = s1
    print(l.getDescription())
    for _ in range(3):
        sNext = l.getNextStop(s)
        print("{0} -> {1}".format(s.getName(), sNext.getName()))
        s = sNext

def tests():
    test_1()
    test_2()
    test_3()
    print("##### DONE #####")

########## ##### ##########

if __name__ == '__main__':
    tests()