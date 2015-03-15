'''
Created on 15/03/2015

@author: Joel Pagliuca
'''
import unittest

tests = unittest.defaultTestLoader.discover("tests", pattern="test_*.py")
runner = unittest.TextTestRunner()
runner.run(tests)