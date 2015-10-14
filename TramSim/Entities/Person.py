'''
Created on 08/03/2014

@author: Joel Pagliuca
'''
import random
from copy import copy
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
        creates a Person with:
            random name
            same Actions
        
        @rtype: Person
        '''
        random_name = random.choice(NAMES)
        new_person = Person(random_name)
        # add the actions
        for a in self.getAllAIActions():
            # TODO: probably a design pattern for this
            copied = copy(a)
            copied.entity = new_person
            new_person.addAIAction(copied)
        for a in self.getAllPlayerActions():
            copied = copy(a)
            copied.entity = new_person
            new_person.addPlayerAction(copied)            
        return new_person