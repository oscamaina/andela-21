import unittest
import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)
from app.dojo import *

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
        self.dojo.create_room("office", ["A04"])
        new_no_offices = len(self.dojo.offices)
        self.assertEqual(new_no_offices-current_no_offices,1)

    def test_adds_living_space_successfully(self):
        """
        Tests if room of type livingSpace can be added successfully
        increases the number of living_spaces.

        """
        current_no_livingSpaces = len(self.dojo.living_spaces)
        living_space =self.dojo.create_room("living", ["Arusha"])
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

    def test_room_created_is_instance_of_room(self):
        """ Should assert room created is an instance of a room """
        self.dojo.create_room("office", ["A04"])
        self.dojo.create_room("living", ["Arusha"])
        self.assertIsInstance(self.dojo.offices[0], Office)
        self.assertIsInstance(self.dojo.living_spaces[0], LivingSpace)

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
        new_no_fellows = len(self.dojo.fellows)
        self.assertEqual(new_no_fellows-current_no_fellows, 1)

    def test_successfully_adds_staff_to_system(self):
        """ Should add staff to the system """
        current_no_staff = len(self.dojo.staffs)
        self.dojo.add_person('Shem','Ogube', 'Staff')
        new_no_staff = len(self.dojo.staffs)
        self.assertEqual(new_no_staff-current_no_staff, 1)

    def test_adding_person_with_invalid_category(self):
        """Tests adding person who's category is not staff or fellow"""
        new = self.dojo.add_person("Wekesa','Maina", "Bootcamper", "N")
        self.assertEqual(new,"Wrong category. Can only be fellow or staff")

    def test_person_added_is_instance_of_person(self):
        """ Should assert the person added is an instance of Person """
        self.dojo.add_person("Mengere", "John", "fellow", "Y")
        self.dojo.add_person("Kipyegon", "Ken", "staff")
        self.assertIsInstance(self.dojo.fellows[0], Fellow)
        self.assertIsInstance(self.dojo.staffs[0], Staff)

class TestPrintingRoom(unittest.TestCase):
    """ Test cases for printing Room and its occupants """
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("office", ["Django"])

    def test_print_room_that_does_not_exist(self):
        """ Should not print a room that is not in the system """
        self.assertEqual(self.dojo.print_room('Entebbe'), \
        "Room Entebbe doesn't exist")

    def test_prints_room_occupants(self):
        """ Should print all the occupants of a specified room """
        self.dojo.add_person('Dennis', 'Wachiuri', 'Fellow')
        self.assertIn("Dennis Wachiuri", self.dojo.print_room('Django'))

    def test_prints_empty_for_unoccupied_room(self):
        """ Prints null if specified room is empty """
        self.assertEqual(self.dojo.print_room('Django'), "Django has no occupants")

class TestPrintAllocatedUnallocated(unittest.TestCase):
    """ Test case for printing allocations """
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.create_room("living", ["Django"])
        # person 1 to 4 should be allocated to living Room Django
        self.dojo.add_person('Dennis', 'Person1', 'Fellow' , 'Y')
        self.dojo.add_person('Dennis', 'Person2', 'Fellow' , 'Y')
        self.dojo.add_person('Dennis', 'Person3', 'Fellow' , 'Y')
        self.dojo.add_person('Dennis', 'Person4', 'Fellow' , 'Y')

        # person 5 should be unallocated
        self.dojo.add_person('Dennis', 'Person5', 'Fellow' , 'Y')

    def test_prints_allocated_successfully(self):
        allocated = self.dojo.print_allocations()
        self.assertIn('DENNIS PERSON4', allocated)

    def test_prints_unallocated_successfully(self):
        unallocated = self.dojo.print_unallocated()
        self.assertIn("Dennis Person5", unallocated)

    def test_print_allocations_with_file_specified(self):
        self.dojo.create_room("office", ["Django"])
        self.dojo.create_room("living", ["Flask"])
        self.dojo.add_person("Maina", "oscar","fellow", "Y")
        self.dojo.add_person("Otieno","Ian","staff")
        allocate = self.dojo.print_allocations("t_file")
        self.assertEqual(allocate, "Data saved in t_file.txt")

    def test_print_unallocated_with_file_specified(self):
        self.dojo.add_person("Maina", "oscar","fellow", "Y")
        self.dojo.add_person("Otieno","Ian","staff")
        unallocate = self.dojo.print_unallocated("t_file")
        self.assertEqual(unallocate, "Data saved in t_file.txt")

class TestReallocatePerson(unittest.TestCase):
    """ Unit tests for reallocating persons """
    def setUp(self):
        self.dojo = Dojo()

    def test_rejects_inavalid_id(self):
        """ Should reject an invalid ID """
        self.dojo.create_room("Office", ["Django"])
        self.dojo.create_room("Office", ["Flask"])
        self.dojo.add_person("mwangi", "james", "fellow")
        F_reallocate = self.dojo.reallocate_person("F", "Flask")
        self.assertEqual(F_reallocate, "Invalid ID")

    def test_rejects_non_existent_id(self):
        """ Should reject an Id that isn't in system """
        self.dojo.create_room("Office", ["Django"])
        self.dojo.create_room("Office", ["Flask"])
        self.dojo.add_person("mwangi", "james", "fellow")
        james_reallocate = self.dojo.reallocate_person(3, "Flask")
        self.assertEqual(james_reallocate, "The person with id 3 doesn't exist")

    def test_rejects_reallocation_to_non_existent_room(self):
        """ Should not reallocate to room that doesn't exist """
        self.dojo.create_room("office", ["PHP"])
        self.dojo.add_person("Ochieng", "Collins", "fellow")
        collins_reallocate = self.dojo.reallocate_person(1, "Java")
        self.assertEqual(collins_reallocate, "room Java doesn't exists")

    def test_rejects_reallocation_to_same_room(self):
        """ Should not reallocate to the same room """
        self.dojo.create_room("office", ["PHP"])
        self.dojo.add_person("Ochieng", "Collins", "fellow")
        collins_reallocate = self.dojo.reallocate_person(1, "PHP")
        self.assertEqual(collins_reallocate, "Can't reallocate to the same room")

    def test_succesfully_reallocates_person(self):
        """ Should reallocate either staff or fellow"""
        self.dojo.create_room("office", ["Django"])
        self.dojo.add_person("Maina", "wekesa", "fellow")
        self.dojo.create_room("office", ["Python"])
        self.assertEqual(self.dojo.reallocate_person(1, "Python"), \
        "Maina wekesa reallocated to Python")

    def test_reallocating_to_full_room(self):
        """ Should not accept rellocating to a full room """
        self.dojo.create_room("living", ["Arusha"])
        self.dojo.add_person("maina", "oscar", "fellow", "Y")
        self.dojo.add_person("ouma", "antony", "fellow", "Y")
        self.dojo.add_person("maasai", "ken", "fellow", "Y")
        self.dojo.add_person("arogo", "robert", "fellow", "Y")
        self.dojo.create_room("living", ["Entebbe"])
        self.dojo.add_person("kioko", "samuel", "fellow", "Y")
        kioko_reallocate = self.dojo.reallocate_person(5, "Arusha")
        self.assertEqual(kioko_reallocate, "Sorry, room Arusha is full")

    def test_reallocating_of_staff_to_livingspace(self):
        """ Should reject relocating staff to a living room """
        self.dojo.create_room("office", ["Java"])
        self.dojo.add_person("mary", "muriga","staff")
        self.dojo.create_room("living", ["kilimanjaro"])
        self.assertEqual(self.dojo.reallocate_person(1, "kilimanjaro"), \
        "Can't rellocate staff to a living room")

class TestLoadPeople(unittest.TestCase):
    """ Unit tests for loading people """
    def setUp(self):
        self.dojo = Dojo()

    def test_load_non_existing_file(self):
        load_non = self.dojo.load_people("files/load.txt")
        self.assertEqual(load_non, "File files/load.txt doesn't exist")

    def test_load_an_empty_file(self):
        load_empty = self.dojo.load_people("files/empty.txt")
        self.assertEqual(load_empty, "File files/empty.txt is empty")

    def test_load_people(self):
        """ Test loading people from a text file. """
        self.dojo.load_people("files/yuti.txt")
        self.assertTrue(os.path.isfile("files/yuti.txt"))
        self.assertEqual(len(self.dojo.all_people), 7)
        self.assertEqual(len(self.dojo.staffs), 3)
        self.assertEqual(len(self.dojo.fellows), 4)
