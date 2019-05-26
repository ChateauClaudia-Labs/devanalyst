import unittest
from unittest import TestCase

import devanalyst.metrics.tests.test_productivity # Import needed to populate tu_.ACTUAL and tu_.EXPECTED

import devanalyst.test_utils.test_utils as tu_

# ----------------------------- Producivity Metrics tests ------------------------------

class test_SimpleProductivity(TestCase):
    def test_no_delay(self):
        self.assertTrue(tu_.testOK('productivity.test_simple.no_delay'))
    def test_meritocratic(self):
        self.assertTrue(tu_.testOK('productivity.test_simple.meritocratic')) 
    def test_work_stealing(self):
        self.assertTrue(tu_.testOK('productivity.test_simple.work_stealing')) 

class test_DragRemoval(TestCase):
    def test_Burnout_with_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Burnout_with_drag'))
    def test_Burnout_without_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Burnout_without_drag'))
    def test_Entries_with_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Entries_with_drag'))
    def test_Entries_without_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Entries_without_drag'))
    def test_Commits_impl_with_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Commits_impl_with_drag'))
    def test_Commits_impl_without_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Commits_impl_without_drag'))
    def test_Commits_bugs_with_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Commits_bugs_with_drag'))
    def test_Commits_bugs_without_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Commits_bugs_without_drag'))
    def test_Commits_all_with_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Commits_all_with_drag'))
    def test_Commits_all_without_drag(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Commits_all_without_drag'))
    def test_Impact(self):
        self.assertTrue(tu_.testOK('productivity.test_drag.Impact'))
