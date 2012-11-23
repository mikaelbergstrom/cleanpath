#!/usr/bin/python
# encoding: UTF-8
import random
import unittest
import sys
import os

sys.path.append( os.path.join( os.getcwd(), '..' ) )
from main import Cleanpath

class TestCleanPath(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_invalidCharsGetsReplaced(self):
        # make sure the shuffled sequence does not lose any elements
        invalidPath = '/Users/mikael.bergstrom/åäö/ÅÄÖ'.decode('utf-8') 
        self.assertEqual(Cleanpath.cleanPath(invalidPath), '/Users/mikael.bergstrom/aao/AAO')

if __name__ == '__main__':
	suite = unittest.TestLoader().loadTestsFromTestCase(TestCleanPath)
	unittest.TextTestRunner(verbosity=4).run(suite)