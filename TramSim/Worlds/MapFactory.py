'''
Created on 09/10/2015

@author: Joel Pagliuca
'''
from TramSim.Worlds import Map, Location, Loop, Stop
from TramSim.Entities import Person, Tram, Spawner, Entity
from TramSim.Actions import SayHi, MoveTramNextStop

class MapFactory(object):
    '''
    Creates maps
    '''
    
    def citymap(self):
        m = Map("City", 15, 10)
        # Locations
        l = Location('City Street')
        for x in range(15):
            for y in range(10):
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
        p = Person("The Guy")
        p.addPlayerAction(SayHi(p))
        m.getLocation(6, 6).addEntity(p)
        t = Tram("Tram", l)
        t.addPlayerAction(MoveTramNextStop(t))
        s1.addEntity(t)
        
        return m