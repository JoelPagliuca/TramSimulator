'''
Created on 17/03/2015

@author: Joel Pagliuca
'''
from TramSim.Actions import Action

class SayHi(Action):
    '''
    Makes an entity say hi
    '''
    
    def canDo(self):
        '''        
        @rtype: bool
        '''
        return True
    
    def do(self):
        '''
        prints Hi
        '''
        print("Hi!")
    
    def getDescription(self):
        return "Have {} say hi".format(self.entity.name)