import unittest
from unittest import TestCase

import devanalyst.simulation.tests.test_timecard as tt


class test_uss(TestCase):
    def test(self):
        self.assertTrue(tt.testOK('uss'))

class test_createTeams(TestCase):
    def test(self):
        self.assertTrue(tt.testOK('createTeams'))


class test_userStoryCreate(TestCase):
    def test_stories_df(self):
        self.assertTrue(tt.testOK('test_userStoryCreate.stories_df'))
    def test_estimates_df(self):
        self.assertTrue(tt.testOK('test_userStoryCreate.estimates_df'))    
    def test_workload_df(self):
        self.assertTrue(tt.testOK('test_userStoryCreate.workload_df'))   
    def test_crosscheck_df(self):
        self.assertTrue(tt.testOK('test_userStoryCreate.crosscheck_df'))    
    def test_avg_estimates_df(self):
        self.assertTrue(tt.testOK('test_userStoryCreate.avg_estimates_df'))



