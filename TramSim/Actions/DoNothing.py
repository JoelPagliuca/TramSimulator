'''
Created on 16/10/2015

@author: Joel Pagliuca
'''
from TramSim.Actions.Action import Action

class DoNothing(Action):
    '''
    Does nothing
    '''

    def canDo(self):
        '''
        you can always do nothing
        '''
        return True

    def do(self):
        pass

    def getDescription(self):
        return "Wait"
        