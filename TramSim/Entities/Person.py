'''
Created on 08/03/2014

@author: Joel Pagliuca
'''
import random
from TramSim.Entities import Entity

NAMES = ["Joel", "Geoffrey", "Edward", "Thomas", "James", "Percy",
         "Jesse", "Gina", "Ellen", "Tabitha", "Jill", "Elizabeth"]

class Person(Entity):
    '''
    Person
    
    representation of a person
    
    PROPERTIES:
        tram
    '''


    def __init__(self, name='Person'):
        '''
        Constructor
        
        @param name: str
        '''
        super().__init__(name)
        self.tram = None
    
    def __str__(self):
        '''
        symbol for the train
        
        @rtype: str
        '''
        return "O"
    
    def clone(self):
        '''
        @rtype: Person
        '''
        random_name = random.choice(NAMES)
        return Person(random_name)