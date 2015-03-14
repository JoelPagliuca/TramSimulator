'''
Created on 13/03/2015

@author: Joel Pagliuca
'''
import unittest

from TramSim.Entities import Loop
from TramSim.Locations import Stop

class TramSimTest(unittest.TestCase):
    '''
    Base unittest for TramSim
    will have a really comprehensive setUp that won't need to be repeated
    because there's currently a lot of repetition in setUp()s and imports
    '''
    
    def setUp(self):
        
        self.loop = Loop('Test Loop')
        
        self.stop1 = Stop('Nigeria')
        self.stop2 = Stop('Brazil')