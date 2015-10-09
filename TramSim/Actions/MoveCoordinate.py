'''
Created on 06/10/2015

@author: Joel Pagliuca
'''
from TramSim.Actions import Action

class MoveCoordinate(Action):
    '''
    Moves an Entity to a coordinate
    '''

    def __init__(self, entity, x, y):
        '''
        Constructor
        '''
        super().__init__(entity)
        self._x = x
        self._y = y
    
    def canDo(self):
        '''
        check if there's a location at the given coordinate
        
        @rtype: bool
        '''
        em = self.entity.EntityManager
        try:
            em.getMap().getLocation(self._x, self._y)
        except:
            # there was no Location
            return False
        
        if self.entity in em.getAllEntities():
            return True
    
    def do(self):
        '''
        tell the em to move the entity
        '''
        em = self.entity.EntityManager
        em.moveEntity(self.entity, self._x, self._y)
    
    def getDescription(self):
        return "Move {} to [{}, {}]".format(self.entity.name, self._x, self._y)