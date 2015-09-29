'''
Created on 29 Sep 2015

@author: Joel Pagliuca
'''
import unittest

tests = unittest.defaultTestLoader.discover("Actions", pattern="test_*.py")
runner = unittest.TextTestRunner()
runner.run(tests)