
import unittest
from app.dojo import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()
        self.second_instance = Dojo()
        self.second_instance.create_room('living', ["kigali"])
        self.second_instance.create_room('office', ["Django"])
        self.second_instance.add_person("Maina", "oscar", "fellow")
        self.second_instance.add_person("Ken", "musomi", "staff")

    def test_successfully_saves_state(self):
        """ Test saves application state to Database. """
        expected = self.second_instance.save_state("somedb")
        self.assertEqual(expected,"App data has been stored in somedb database")

    def test_successfully_load_state(self):
        """ Test loading data from database to application """
        #dojo instance should receive data saved in somedb.db
        self.dojo.load_state("somedb")
        self.assertEqual(len(self.dojo.all_rooms),2)
        self.assertEqual(len(self.dojo.all_people),2)

        #second_instance should have data saved
        self.second_instance.load_state("somedb")
        self.assertEqual(len(self.second_instance.all_rooms),2)
        self.assertEqual(len(self.second_instance.all_people),2)

    def test_load_state_from_non_existing_database(self):
        """Tests for loading state from a database that doesn't exist"""
        self.assertEqual(self.dojo.load_state("dcea"), "dcea does not exist")
        self.assertEqual(len(self.dojo.all_rooms),0)
