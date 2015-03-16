'''
Created on 16/03/2015

@author: Joel Pagliuca
'''
import unittest

tests = unittest.defaultTestLoader.discover("Control", pattern="test_*.py")
runner = unittest.TextTestRunner()
runner.run(tests)