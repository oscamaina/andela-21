import os
from random import choice

from app.rooms import Room, Office, LivingSpace
from app.person import Person, Fellow, Staff


class Dojo():

	def __init__(self):
		self.all_rooms = []
		self.offices = []
		self.living_spaces = []
		self.all_people = []
		self.fellows = []
		self.staffs = []
		self.waiting_to_allocate_living = []
		self.waiting_to_allocate_office = []

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
				if room_type == 'office':
					room = Office(room_name)
					self.offices.append(room)
					self.all_rooms.append(room)
					msg += "Office " + room_name + " added successfully \n"
				elif room_type == 'living':
					room = LivingSpace(room_name)
					self.living_spaces.append(room)
					self.all_rooms.append(room)
					msg += "Living space " + room_name + " added successfully\n"
				else:
					msg += "Wrong room type \n"
		return msg


	def add_person(self, first_name, last_name, category, accomodation="N"):
		""" function to add a person """
		if isinstance(first_name, str) and isinstance(last_name, str):
			if category.lower() == "fellow":
				person = Fellow(first_name, last_name, accomodation)
				person.id = int(len(self.all_people)+1)
				self.fellows.append(person)
				self.all_people.append(person)
				self.waiting_to_allocate_office.append(person)
				if accomodation.upper() == 'Y':
					self.waiting_to_allocate_living.append(person)
					return "Fellow " + person.first_name + " " + \
					 person.last_name + " added successfully with id " \
					 + str(person.id) + ", " + str(self.allocate_office(person)) \
					 + " and " + str(self.allocate_living(person))
				return "Fellow " + person.first_name + " " + person.last_name\
				 + " added successfully with id " + str(person.id) + " and " \
				+ str(self.allocate_office(person))

			elif category.lower() == "staff":
				if accomodation.upper() == "Y":
					return "Sorry! staff can't be accomodated"
				else:
					person = Staff(first_name, last_name)
					person.id = int(len(self.all_people)+1)
					self.staffs.append(person)
					self.all_people.append(person)
					self.waiting_to_allocate_office.append(person)
					return "Staff " + person.first_name + " " + \
					person.last_name + " added successfully with id " \
					+ str(person.id) + " and " + str(self.allocate_office(person))
			else:
				return "Wrong category. Can only be fellow or staff"
		else:
			return "Invalid name"

	def allocate_office(self, person):
		""" Allocates office to person added """

		office_with_space = []
		#filters offices and returns offices with space
		for office_allocate in self.offices:
			if len(office_allocate.occupants) < office_allocate.max_capacity:
				office_with_space.append(office_allocate)

		if len(office_with_space) > 0:
			random_office = choice(office_with_space)
			random_office.occupants.append(person)
			self.waiting_to_allocate_office.remove(person)
			return "allocated to " + random_office.room_name \
				 + " Office space"
		else:
			return "No offices with space available"

	def allocate_living(self, person):
		""" Allocates living space to fellow added """

		living_with_space = []
		#filters living_spaces and returns ones with space
		for living_allocate in self.living_spaces:
			if len(living_allocate.occupants) < living_allocate.max_capacity:
				living_with_space.append(living_allocate)

		if len(living_with_space) > 0:
			random_living_space = choice(living_with_space)
			random_living_space.occupants.append(person)
			self.waiting_to_allocate_living.remove(person)
			return "allocated to " + random_living_space.room_name \
			 + " Living space"
		else:
			return "No living rooms with space available"
