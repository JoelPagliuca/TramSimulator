'''
Created on 14/03/2015

@author: Joel Pagliuca
'''
import unittest

tests = unittest.defaultTestLoader.discover("Entities", pattern="test_*.py")
runner = unittest.TextTestRunner()
runner.run(tests)