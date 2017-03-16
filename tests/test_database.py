
import unittest
from app.dojo import *


class TestDatabase(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_successfully_saves_state(self):
        """ Test saves application state to Database. """
        self.dojo.create_room('living', ["kigali"])
        self.dojo.create_room('office', ["Django"])
        self.dojo.add_person("Maina", "oscar", "fellow")
        self.dojo.add_person("Ken", "musomi", "staff")
        output = self.dojo.save_state("somedb.db")

        #connect to db and create session
        engine = create_engine('sqlite:///database/somedb.db')
        sessionDB = sessionmaker(bind=engine)
        session = sessionDB()

        #querry if data is saved
        rooms = session.query(RoomModel).all()
        persons = session.query(PersonModel).all()

        self.assertEqual(len(rooms),2)
        self.assertEqual(len(persons),2)
        self.assertEqual(output,"App data has been stored in somedb.db database")

    def test_successfully_load_state(self):
        """ Test loading data from database to application """
        self.dojo.load_state("flask.db")
        self.assertEqual(len(self.dojo.all_rooms),8)
        self.assertEqual(len(self.dojo.all_people),0)

    def test_load_state_with_non_existing_database(self):
        """Tests for loading state with a database that doesn't exist"""
        self.assertEqual(self.dojo.load_state("dcea"), "dcea does not exist")
