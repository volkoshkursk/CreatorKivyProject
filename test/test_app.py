'''
This file is responsible for testing Apps inside the CreatorKivyProject project.
'''

import os
import sys
import unittest


class AppTest(unittest.TestCase):

    def test_creator_app(self):
        sys.path.insert(0, os.path.split(os.path.abspath(sys.argv[0]))[0])
        from test import Test
        test = Test()
        test.run()
