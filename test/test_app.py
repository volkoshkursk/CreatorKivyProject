'''
This file is responsible for testing Apps inside the CreatorKivyProject project.
'''

import unittest


class AppTest(unittest.TestCase):

    def test_creator_app(self):
        from test import Test
        test = Test()
        test.run()
