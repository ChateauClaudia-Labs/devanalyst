import unittest
from unittest import TestCase

import devanalyst.simulation.tests.test_simm # Import needed to populate tu_.ACTUAL and tu_.EXPECTED

import devanalyst.test_utils.test_utils as tu_

# ----------------------------- Simulation Model tests ------------------------------

class test_greedyAllocationLogs(TestCase):
    def test_Committed(self):
        self.assertTrue(tu_.testOK('simm.test_greedyAllocationLogs'))

class test_greedyAllocation(TestCase):
    def test_Committed(self):
        self.assertTrue(tu_.testOK('simm.test_greedyAllocation.Committed'))
    def test_Tasks(self):
        self.assertTrue(tu_.testOK('simm.test_greedyAllocation.Tasks')) 

class test_balancedAllocation(TestCase):
    def test_Committed(self):
        self.assertTrue(tu_.testOK('simm.test_balancedAllocation.Committed'))
    def test_Tasks(self):
        self.assertTrue(tu_.testOK('simm.test_balancedAllocation.Tasks')) 

class test_noLaggardsAllocation(TestCase):
    def test_Committed(self):
        self.assertTrue(tu_.testOK('simm.test_noLaggardsAllocation.Committed'))
    def test_Tasks(self):
        self.assertTrue(tu_.testOK('simm.test_noLaggardsAllocation.Tasks')) 

class test_distributedLagQualityModel(TestCase):
    def test_bugs(self):
        self.assertTrue(tu_.testOK('simm.test_distributedLagQualityModel.bugs'))
    def test_stories(self):
        self.assertTrue(tu_.testOK('simm.test_distributedLagQualityModel.stories')) 
