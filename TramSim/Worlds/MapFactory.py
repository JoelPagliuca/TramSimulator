'''
Created on 09/10/2015

@author: Joel Pagliuca
'''
from TramSim.Worlds import Map, Location, Loop, Stop
from TramSim.Entities import Person, Tram
from TramSim.Actions import MovePersonRandom, MoveTramNextStop, BoardTram, LeaveTram

from random import randint

class MapFactory(object):
    '''
    Creates maps
    '''
    
    def citymap(self):
        width = 15
        height = 10
        m = Map("City", width, height)
        # Locations
        l = Location('City Street')
        for x in range(width):
            for y in range(height):
                m.addLocation(l.clone(), x, y)
        # Stops
        s1 = Stop("Stop 1")
        s1.setSymbol("1")
        s2 = Stop("Stop 2")
        s2.setSymbol("2")
        s3 = Stop("Stop 3")
        s3.setSymbol("3")
        s4 = Stop("Stop 4")
        s4.setSymbol("4")
        m.addLocation(s1, 3, 3)
        m.addLocation(s2, 12, 3)
        m.addLocation(s3, 12, 7)
        m.addLocation(s4, 3, 7)
        # Loop
        l = Loop("City Loop")
        l.addStop(s1)
        l.addStop(s2)
        l.addStop(s3)
        l.addStop(s4)
        # Entities
        t = Tram("Tram", l)
        t.addPlayerAction(MoveTramNextStop(t))
        s1.addEntity(t)
        p = Person("The Original")
        p.addPlayerAction(MovePersonRandom(p))
        p.addPlayerAction(BoardTram(p, t))
        p.addPlayerAction(LeaveTram(p))
        for _ in range(5):
            m.getLocation(randint(0, width-1), randint(0, height-1)).addEntity(p.clone())
        
        return m