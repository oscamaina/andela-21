import unittest
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from app.dojo import Dojo
from app.rooms import Office, LivingSpace
from app.person import Fellow, Staff

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
        self.assertIsInstance(room, Office)
        new_no_offices = len(self.dojo.offices)
        self.assertEqual(office, "Office a04 added successfully \n")
        self.assertEqual(new_no_offices-current_no_offices,1)

    def test_adds_living_space_successfully(self):
        """
        Tests if room of type livingSpace can be added successfully
        increases the number of living_spaces.

        """
        current_no_livingSpaces = len(self.dojo.living_spaces)
        living_space =self.dojo.create_room("living", ["Arusha"])
        room = LivingSpace('java')
        self.assertIsInstance(room, LivingSpace)
        new_no_livingSpaces = len(self.dojo.living_spaces)
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
        self.dojo.add_person('Kipyegon','ken', 'Fellow')
        person = Fellow('Maina','Wekesa')
        self.assertIsInstance(person, Fellow)
        new_no_fellows = len(self.dojo.fellows)
        self.assertEqual(new_no_fellows-current_no_fellows, 1)

    def test_successfully_adds_staff_to_system(self):
        """ Should add staff to the system """
        current_no_staff = len(self.dojo.staffs)
        self.dojo.add_person('Shem','Ogube', 'Staff')
        person = Staff('Ken','Kipyegon')
        self.assertIsInstance(person, Staff)
        new_no_staff = len(self.dojo.staffs)
        self.assertEqual(new_no_staff-current_no_staff, 1)

    def test_adding_person_with_invalid_category(self):
        """Tests adding person who's category is not staff or fellow"""
        new = self.dojo.add_person("Wekesa','Maina", "Bootcamper", "N")
        self.assertEqual(new,"Wrong category. Can only be fellow or staff")

class TestPrintingRoom(unittest.TestCase):
    """ Test cases for printing Room and its occupants """
    def setUp(self):
        self.dojo = Dojo()

    def test_print_room_that_does_not_exist(self):
        """ Should not print a room that is not in the system """
        room_print = self.dojo.print_room('Entebbe')
        self.assertEqual(room_print, "Room name Entebbe doesn't exist")

    def test_prints_room_occupants(self):
        """ Should print all the occupants of a specified room """
        self.dojo.create_room("office", ["Django"])
        self.dojo.add_person('Dennis', 'Wachiuri', 'Fellow')
        room=self.dojo.print_room('Django')
        self.assertIn("Dennis Wachiuri", "room")

    def test_prints_empty_for_unoccupied_room(self):
        """ Prints null if specified room is empty """
        self.dojo.create_room("office", ["Django"])
        r_print = self.dojo.print_room('Django')
        self.assertEqual(r_print, "Django has no occupants")

class TestPrintAllocatedUnallocated(unittest.TestCase):
    """ Test case for printing allocations """
    def setUp(self):
        self.dojo = Dojo()

    def test_prints_allocations_successfully(self):
        """ should return allocated persons and unallocated persons"""
        self.dojo.create_room("living", ["Django"])
        # person 1 to 4 should be allocated to living Room Django
        self.dojo.add_person('Dennis', 'Person1', 'Fellow', 'Y')
        self.dojo.add_person('Dennis', 'Person2', 'Fellow', 'Y')
        self.dojo.add_person('Dennis', 'Person3', 'Fellow', 'Y')
        self.dojo.add_person('Dennis', 'Person4', 'Fellow', 'Y')

        # person 5 should be unallocated
        self.dojo.add_person('Dennis', 'Person5', 'Fellow' 'Y')

        allocated = self.dojo.print_allocations()
        unallocated = self.dojo.print_unallocated()
        self.assertIn('Dennis Person5', allocated)
        self.assertIn("Dennis Person7", unallocated)
