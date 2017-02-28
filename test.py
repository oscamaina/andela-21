import unittest
from dojo import Dojo

class TestCreateRoom(unittest.TestCase):
    """Test cases for creating room"""
    def setUp(self):
        self.dojo = Dojo()

    def test_adds_office_successfully(self):
        """Tests if room of type office can be added successfully"""
        office = self.dojo.create_room("office", "A04")
        self.assertEqual(office, "Office added successfully")

    def test_adds_living_space_successfully(self):
        """Tests if room of type livingSpace can be added successfully"""
        living_space =self.dojo.create_room("living_space", "Arusha")
        self.assertEqual(living_space, "Living space added successfully")

    def test_room_exists(self):
        """Tests if room already exists"""
        self.dojo.create_room("office", "Bujumbura")
        room =self.dojo.create_room("office", "Bujumbura")
        self.assertEqual(room,"Room already exists")

    def test_create_wrong_room_type(self):
        """Tests adding wrong room type """
        room = self.dojo.create_room("social_hall", "Stam")
        self.assertEqual(room, "Wrong room type")

class TestAddingPersons(unittest.TestCase):
    """Test cases for Adding Persons"""
    def setUp(self):
        self.dojo = Dojo()
        self.dojo.fellows = []
        self.dojo.staffs = []

    def test_successfully_adds_fellow_to_system(self):
        """ Should add fellow to the system """
        current_no_fellows = len(self.dojo.fellows)
        self.dojo.add_person('Kipyegon Ken', 'Fellow')
        new_no_fellows = len(self.dojo.fellows)
        self.assertEqual(new_no_fellows, current_no_fellows+1)

    def test_successfully_adds_staff_to_system(self):
        """ Should add staff to the system """
        current_no_staff = len(self.dojo.staffs)
        self.dojo.add_person('Shem Ogube', 'Staff')
        new_no_staff = len(self.dojo.staffs)
        self.assertEqual(new_no_staff, current_no_staff+1)

    def test_adding_person_with_invalid_category(self):
        """Tests adding person who's category is not staff or fellow"""
        new = self.dojo.add_person("Wekesa Maina", "Bootcamper", "N")
        self.assertEqual(new,"Wrong input. Can only be FELLOW or STAFF")

    def test_staff_can_not_be_given_accomodation(self):
        """ Should not add staff with allocated accomodation """
        self.dojo.create_room("living_space", "Kilimanjaro")
        staff = self.dojo.add_person("Ochieng Collins", "Staff", "Y")
        self.assertEqual(staff, "staff cannot be created")
        
    def test_add_person_that_already_exist(self):
        """ Should not duplicate persons """
        self.dojo.add_person("Millicent Njuguna", "Fellow", "Y")
        new = self.dojo.add_person("Millicent Njuguna", "Fellow", "Y")
        self.assertEqual(new, "Person already exists")

if __name__ == '__main__':
    unittest.main()