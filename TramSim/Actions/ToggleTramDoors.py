'''
Created on 16/10/2015

@author: Joel Pagliuca
'''
from TramSim.Actions.Action import Action

class ToggleTramDoors(Action):
    '''
    Toggle tram doors
    probably a safe action
    '''

    def canDo(self):
        '''
        should always be allowed
        assuming the given entity is a Tram
        '''
        return True

    def do(self):
        '''
        open if they're closed
        close if they're open
        '''
        if self.entity.doorsOpen():
            self.entity.closeDoors()
        else:
            self.entity.openDoors()

    def getDescription(self):
        '''
        also based on tram door status
        '''
        if self.entity.doorsOpen():
            d = "Close {} doors"
        else:
            d = "Open {} doors"
        return d.format(self.entity.name)