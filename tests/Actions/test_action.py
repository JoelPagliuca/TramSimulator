'''
Created on 29 Sep 2015

@author: Joel Pagliuca
'''
import unittest

from tests.TramSimTest import TramSimTest

class TestAction(TramSimTest):

    def test_unimplementedExceptionss(self):
        for method in ['canDo', 'do', 'getDescription']:
            f = getattr(self.action, method)
            self.assertRaises(NotImplementedError, f)

if __name__ == "__main__":
    unittest.main()