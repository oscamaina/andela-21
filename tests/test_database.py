
import unittest
from app.dojo import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.fDojo = Dojo()
        self.fDojo.create_room('living', ["kigali"])
        self.fDojo.create_room('office', ["Django"])
        self.fDojo.add_person("Maina", "oscar", "fellow")
        self.fDojo.add_person("Ken", "musomi", "staff")

    def test_successfully_saves_state(self):
        """ Test saves application state to Database. """
        expected = self.dojo.save_state("somedb.db")
        self.assertEqual(expected,"App data has been stored in somedb.db database")

    def test_successfully_load_state(self):
        """ Test loading data from database to application """
        expected = self.fDojo.load_state("somedb.db")
        self.assertEqual(len(self.fDojo.all_rooms),2)
        self.assertEqual(len(self.fDojo.all_people),2)

    def test_load_state_from_non_existing_database(self):
        """Tests for loading state from a database that doesn't exist"""
        self.assertEqual(self.dojo.load_state("dcea"), "dcea does not exist")
        self.assertEqual(len(self.dojo.all_rooms),0)
