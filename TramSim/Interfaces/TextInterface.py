'''
Created on 16/03/2015

@author: Joel Pagliuca
'''
from TramSim.Interfaces import UserInterface

class TextInterface(UserInterface):
    '''
    '''
    
    def render(self, obj):
        '''
        prints the object to stdout
        '''
        print(obj, end="")