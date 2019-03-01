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

class test_WorkAssignments(TestCase):
    def test_Initial(self):
        self.assertTrue(tt.testOK('test_WorkAssignments.Initial'))
    def test_Final(self):
        self.assertTrue(tt.testOK('test_WorkAssignments.Final')) 

class test_greedyAllocation(TestCase):
    def test_Committed(self):
        self.assertTrue(tt.testOK('test_greedyAllocation.Committed'))
    def test_Tasks(self):
        self.assertTrue(tt.testOK('test_greedyAllocation.Tasks'))   

class test_oneSprint(TestCase):
    def test_Start_Committed(self):
        self.assertTrue(tt.testOK('test_oneSprint.Start_Committed'))
    def test_Start_Tasks(self):
        self.assertTrue(tt.testOK('test_oneSprint.Start_Tasks'))  
    def test_End_Committed(self):
        self.assertTrue(tt.testOK('test_oneSprint.End_Committed'))
    def test_End_Tasks(self):
        self.assertTrue(tt.testOK('test_oneSprint.End_Tasks'))  

class test_multipleSprints(TestCase):
    def test_start_committed(self):
        self.assertTrue(tt.testOK('test_multipleSprints.start_committed'))
    def test_start_tasks(self):
        self.assertTrue(tt.testOK('test_multipleSprints.start_tasks'))  
    def test_end_committed(self):
        self.assertTrue(tt.testOK('test_multipleSprints.end_committed'))
    def test_end_tasks(self):
        self.assertTrue(tt.testOK('test_multipleSprints.end_tasks'))

class test_releaseCycle(TestCase):
    def test_Entries(self):
        self.assertTrue(tt.testOK('test_releaseCycle.Entries'))
    def test_Anton(self):
        self.assertTrue(tt.testOK('test_releaseCycle.Anton'))  
    def test_Glenna(self):
        self.assertTrue(tt.testOK('test_releaseCycle.Glenna'))
    def test_Burnout(self):
        self.assertTrue(tt.testOK('test_releaseCycle.Burnout'))

# This does not test the functionality, but just the test template to ensure that if someone
# copies-and-pastes it to define a new test, at least it is going to compile and run
class test_testTemplate(TestCase):
    def test_A(self):
        self.assertTrue(tt.testOK('test_FOO.Dummy_A'))
    def test_B(self):
        self.assertTrue(tt.testOK('test_FOO.Dummy_B'))

