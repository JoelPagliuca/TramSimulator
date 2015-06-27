'''
Created on 08/03/2014

@author: Joel Pagliuca
'''

class Person:
    '''
    Person
    
    representation of a person
    
    PROPERTIES:
    '''


    def __init__(self, name = 'Person'):
        '''
        Constructor
        '''
        super().__init__(name)
    
    def __str__(self):
        '''
        '''
        return "O"