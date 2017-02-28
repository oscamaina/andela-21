import unittest
from dojo import Dojo

class TestAddingRoom(unittest.TestCase):
    def setUp(self):
        self.dojo = Dojo()

    def test_adds_office_successfully(self):
        """Tests if room of type office is added successfully"""
        office = self.dojo.create_room("office", "A04")
        self.assertEqual(office, "Office added successfully")

    def test_adds_living_space_successfully(self):
        """Tests if room of type livingSpace is added successfully"""
        living_space =self.dojo.create_room("living_space", "Arusha")
        self.assertEqual(living_space, "Living space added successfully")

    def test_room_exists(self):
        """Tests if room already exists"""
        room =self.dojo.create_room("office", "Bujumbura")
        self.assertEqual(room,"Room already exists")

if __name__ == '__main__':
    unittest.main()