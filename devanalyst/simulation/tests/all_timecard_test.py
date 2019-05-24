import unittest
from unittest import TestCase

import devanalyst.simulation.tests.test_timecard # Import needed to populate tu_.ACTUAL and tu_.EXPECTED

import devanalyst.test_utils.test_utils as tu_

# --------------------------------- Timecard tests ----------------------------------
class test_uss(TestCase):
    def test(self):
        self.assertTrue(tu_.testOK('uss'))

class test_createTeams(TestCase):
    def test(self):
        self.assertTrue(tu_.testOK('createTeams'))


class test_userStoryCreate(TestCase):
    def test_stories_df(self):
        self.assertTrue(tu_.testOK('test_userStoryCreate.stories_df'))
    def test_estimates_df(self):
        self.assertTrue(tu_.testOK('test_userStoryCreate.estimates_df'))    
    def test_workload_df(self):
        self.assertTrue(tu_.testOK('test_userStoryCreate.workload_df'))   
    def test_crosscheck_df(self):
        self.assertTrue(tu_.testOK('test_userStoryCreate.crosscheck_df'))    
    def test_avg_estimates_df(self):
        self.assertTrue(tu_.testOK('test_userStoryCreate.avg_estimates_df'))

class test_WorkAssignments(TestCase):
    def test_Initial(self):
        self.assertTrue(tu_.testOK('test_WorkAssignments.Initial'))
    def test_Final(self):
        self.assertTrue(tu_.testOK('test_WorkAssignments.Final'))  

class test_oneSprint(TestCase):
    def test_Start_Committed(self):
        self.assertTrue(tu_.testOK('test_oneSprint.Start_Committed'))
    def test_Start_Tasks(self):
        self.assertTrue(tu_.testOK('test_oneSprint.Start_Tasks'))  
    def test_End_Committed(self):
        self.assertTrue(tu_.testOK('test_oneSprint.End_Committed'))
    def test_End_Tasks(self):
        self.assertTrue(tu_.testOK('test_oneSprint.End_Tasks'))  

class test_multipleSprints(TestCase):
    def test_start_committed(self):
        self.assertTrue(tu_.testOK('test_multipleSprints.start_committed'))
    def test_start_tasks(self):
        self.assertTrue(tu_.testOK('test_multipleSprints.start_tasks'))  
    def test_end_committed(self):
        self.assertTrue(tu_.testOK('test_multipleSprints.end_committed'))
    def test_end_tasks(self):
        self.assertTrue(tu_.testOK('test_multipleSprints.end_tasks'))

class test_releaseCycle(TestCase):
    def test_Entries(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.Entries'))
    def test_Burnout(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.Burnout'))
    def test_planned_Start_CURRENT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.planned_Start_CURRENT_SPRINT'))  
    def test_planned_End_CURRENT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.planned_End_CURRENT_SPRINT'))  
    def test_planned_Start_NEXT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.planned_Start_NEXT_SPRINT'))  
    def test_planned_End_NEXT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.planned_End_NEXT_SPRINT'))  
    def test_backlog(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.backlog'))  
    def test_Resourcing(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.Resourcing'))   
    def test_Outcome(self):
        self.assertTrue(tu_.testOK('test_releaseCycle.Outcome')) 

class test_buggyReleaseCycle(TestCase):
    def test_Entries(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.Entries'))
    def test_User_Stories(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.User_Stories'))
    def test_Tickets(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.Tickets'))
    def test_Burnout(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.Burnout'))
    def test_planned_Start_CURRENT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.planned_Start_CURRENT_SPRINT'))  
    def test_planned_End_CURRENT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.planned_End_CURRENT_SPRINT'))  
    def test_planned_Start_NEXT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.planned_Start_NEXT_SPRINT'))  
    def test_planned_End_NEXT_SPRINT(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.planned_End_NEXT_SPRINT'))  
    def test_backlog(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.backlog'))  
    def test_Resourcing(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.Resourcing'))   
    def test_Outcome(self):
        self.assertTrue(tu_.testOK('test_buggyReleaseCycle.Outcome'))   


