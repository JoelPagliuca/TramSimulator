'''
Created on 16/03/2015

@author: Joel Pagliuca
'''

class UserInterface:
    '''
    ABSTRACT
    will be a generic interface so I can replace a text interface with a gui
    '''


    def render(self):
        raise NotImplementedError("UserInterface: Abstract method render not defined")