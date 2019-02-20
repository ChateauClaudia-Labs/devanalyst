import unittest
from unittest import TestCase

import devanalyst.simulation.tests.test_timecard as tt


class test_uss(TestCase):

    def test(self):
        self.assertTrue(tt.test_uss_ACTUAL == tt.test_uss_EXPECTED)


class test_fail(TestCase):

    def test(self):
        self.assertTrue(1 == 2)

class test_pass(TestCase):

    def test(self):
        self.assertTrue(2 == 2)

