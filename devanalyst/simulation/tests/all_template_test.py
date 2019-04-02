import unittest
from unittest import TestCase

import devanalyst.simulation.tests.test_template # Import needed to populate tu_.ACTUAL and tu_.EXPECTED

import devanalyst.simulation.tests.test_utils as tu_

# --------------------------------- Template tests ----------------------------------

# This does not test the functionality, but just the test template to ensure that if someone
# copies-and-pastes it to define a new test, at least it is going to compile and run
class test_testTemplate(TestCase):
    def test_A(self):
        self.assertTrue(tu_.testOK('test_FOO.Dummy_A'))
    def test_B(self):
        self.assertTrue(tu_.testOK('test_FOO.Dummy_B'))

