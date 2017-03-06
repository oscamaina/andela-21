import unittest
from dojo import Dojo
from rooms import Room, Office, LivingSpace

class TestCreateRoom(unittest.TestCase):
    """Test cases for creating room"""
    def setUp(self):
        self.dojo = Dojo()

    def test_adds_office_successfully(self):
        """
        Tests if room of type office can be added successfully
        it should the increase the number of offices.

        """
        current_no_offices = len(self.dojo.offices)
        office = self.dojo.create_room("office", ["A04"])
        room = Office('kigali')
        self.assertIsInstance(room, Room)
        new_no_offices = len(self.dojo.offices)
        self.assertEqual(office, "Office a04 added successfully \n")
        self.assertEqual(new_no_offices-current_no_offices,1)

    def test_adds_living_space_successfully(self):
        """
        Tests if room of type livingSpace can be added successfully
        increases the number of living_spaces.

        """
        current_no_livingSpaces = len(self.dojo.livingSpaces)
        living_space =self.dojo.create_room("living", ["Arusha"])
        room = LivingSpace('java')
        self.assertIsInstance(room, Room)
        new_no_livingSpaces = len(self.dojo.livingSpaces)
        self.assertEqual(living_space, "Living space arusha added successfully\n")
        self.assertEqual(new_no_livingSpaces-current_no_livingSpaces,1)

    def test_creating_room_that_exists(self):
        """Should not accept duplicating rooms"""
        self.dojo.create_room("office", ["Bujumbura"])
        room =self.dojo.create_room("office", ["Bujumbura"])
        self.assertEqual(room,"Room with name bujumbura already exists \n")

    def test_create_wrong_room_type(self):
        """
        Tests adding wrong room type
        should not increase the number of rooms

        """
        current_no_rooms = len(self.dojo.all_rooms)
        room = self.dojo.create_room("social_hall", ["Stam"])
        new_no_rooms = len(self.dojo.all_rooms)
        self.assertEqual(room, "Wrong room type \n")
        self.assertEqual(current_no_rooms, new_no_rooms)

class TestAddingPersons(unittest.TestCase):
    """Test cases for Adding Persons"""
    def setUp(self):
        self.dojo = Dojo()

    def test_successfully_adds_fellow_to_system(self):
        """
        Should add fellow to the system
        and increase the number of fellows

        """
        current_no_fellows = len(self.dojo.fellows)
        self.dojo.add_person('Kipyegon Ken', 'Fellow')
        new_no_fellows = len(self.dojo.fellows)
        self.assertEqual(new_no_fellows-current_no_fellows, 1)

    def test_successfully_adds_staff_to_system(self):
        """ Should add staff to the system """
        current_no_staff = len(self.dojo.staffs)
        self.dojo.add_person('Shem Ogube', 'Staff')
        new_no_staff = len(self.dojo.staffs)
        self.assertEqual(new_no_staff-current_no_staff, 1)

    def test_adding_person_with_invalid_category(self):
        """Tests adding person who's category is not staff or fellow"""
        new = self.dojo.add_person("Wekesa Maina", "Bootcamper", "N")
        self.assertEqual(new,"Wrong category. Can only be fellow or staff")
