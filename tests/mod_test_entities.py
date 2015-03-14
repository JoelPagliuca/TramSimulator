'''
Created on 29/12/2014

@author: Joel Pagliuca
'''
import unittest

# from tests.Entities import test_loop, test_tram
# 
# suite_loop = unittest.defaultTestLoader.loadTestsFromModule(test_loop)
# suite_tram = unittest.defaultTestLoader.loadTestsFromModule(test_tram)
#  
# all_tests = unittest.TestSuite([suite_loop, suite_tram])
# 
# runner = unittest.TextTestRunner()
# runner.run(all_tests)

# I'm gonna leave this here because it is still interesting

tests = unittest.defaultTestLoader.discover("Entities", pattern="test_*.py")
runner = unittest.TextTestRunner()
runner.run(tests)