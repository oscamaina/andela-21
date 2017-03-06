from random import choice
from rooms import Room, Office, LivingSpace
from person import Person, Fellow, Staff


class Dojo():

	def __init__(self):
		self.all_rooms = []
		self.offices = []
		self.livingSpaces = []
		self.all_people = []
		self.fellows = []
		self.staffs = []

	def create_room(self, room_type, room_names):
		""" function to create a unique room space """
		msg = ''
		for name in room_names:
			room_name = name.lower()
			room_type = room_type.lower()

			found = False
			for room in self.all_rooms:
				if room_name == room.room_name:
					found = True
			if found:
				msg += "Room with name " + room_name + " already exists \n"
			else:
				if room_type in ('office', 'living'):
					room = Room(room_name)
					self.all_rooms.append(room)
				if room_type == 'office':
					room = Office(room_name)
					self.offices.append(room)
					msg += "Office " + room_name + " added successfully \n"
				elif room_type == 'living':
					room = LivingSpace(room_name)
					self.livingSpaces.append(room)
					msg += "Living space " + room_name + " added successfully\n"
				else:
					msg += "Wrong room type \n"
			return msg


	def add_person(self, first_name, last_name, category, accomodation="N"):
		""" function to add a person """
		full_name = first_name.capitalize() + " " + last_name.capitalize()
		category = category.lower()
		accomodation = accomodation.upper()

		if category in ("fellow", "staff"):

			id = len(self.all_people) + 1
			person = Person(first_name, last_name)
			self.all_people.append(person)
		if category == "fellow":
			person = Fellow(first_name, last_name, accomodation)
			self.fellows.append(person)
			if accomodation == 'Y':
				return "Fellow added successfully with id " + str(id) + ". " \
				+ self.allocate_office(full_name) + ". " + \
				self.allocate_living(full_name)
			return "Fellow added successfully with id " + str(id) + ". " \
			+ self.allocate_office(full_name)

		elif category == "staff":
			person = Staff(first_name, last_name)
			if accomodation == "Y":
				return "Sorry! staff can't be accomodated"
			else:
				self.staffs.append(person)
				return "Staff added successfully with id " + str(id) + ". " \
				+ self.allocate_office(full_name)
		else:
			return "Wrong category. Can only be fellow or staff"

	def allocate_office(self, full_name):
		""" Allocates office to person added """

		if len(self.offices) > 0:
			office_allocate = choice(self.offices)
			if len(office_allocate.occupants) < office_allocate.max_capacity:
				office_allocate.occupants.append(full_name)
				return "Allocated " + full_name + " to " + \
				office_allocate.room_name + " office"
			else:
				return "No offices with space"
		else:
			return "No available offices"

	def allocate_living(self, full_name):
		""" Allocates living space to fellow added """
		if len(self.livingSpaces) > 0:
			living_allocate = choice(self.livingSpaces)
			if len(living_allocate.occupants) < living_allocate.max_capacity:
				living_allocate.occupants.append(full_name)
				return "Allocated " + full_name + " to " + \
				living_allocate.room_name + " Living space"
			else:
				return "No Living rooms with space"
		else:
			return "No available living rooms"
