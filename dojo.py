from random import randint
from rooms import Office, LivingSpace
from person import Fellow, Staff

class Dojo():

	def __init__(self):
		self.rooms = []
		self.offices = []
		self.livingSpaces = []
		self.persons = []
		self.fellows = []
		self.staffs = []

	def create_room(self, room_type, room_names):
		""" function to create a unique room space """
		msg = ''
		for name in room_names:
			room_name = name.lower()
			room_type = room_type.lower()
			occupants = []
			room_capacity = (6 if room_type=='office' else 4)

			current_rooms = []
			for room in self.rooms:
				current_rooms.append(room['room_name'])
			if room_name in current_rooms:
				msg += "Room with name " + room_name + " already exists \n"
			else:
				if room_type in ('office', 'living'):
					self.rooms.append({'room_name': room_name, 'occupants': occupants, 'type': room_type, 'room_capacity': room_capacity})
					if room_type == 'office':
						room = Office(room_name)
						self.offices.append({'room_name': room_name, 'occupants': occupants, 'room_capacity': room_capacity})
						msg += "Office " + room_name + " added successfully \n"
					elif room_type == 'living':
						room = LivingSpace(room_name)
						self.livingSpaces.append({'room_name': room_name, 'occupants': occupants, 'room_capacity': room_capacity})
						msg += "Living space " + room_name + " added successfully \n"
				else:
					msg += "Wrong room type \n"
		return msg

		
	def add_person(self, name, category, accomodation="N"):
		""" function to add a person """
		name = name.lower()
		category = category.lower()
		accomodation = accomodation.upper()

		people = []
		for person in self.fellows:
			people.append(person['name'])
		for person in self.staffs:
			people.append(person['name'])
		if name in people:
			choice = input(name + " has already been used, Enter Y to proceed or C to cancel:")
			if choice.upper() not in ['Y', 'C']:
				return "Invalid choice"
			elif choice.upper() == 'C':
				return "Bye"
		if category in ("fellow", "staff"):
			
			id = len(self.persons) + 1
			self.persons.append({'name': name, 'id': id})
			if category == "fellow":
				person = Fellow(name, accomodation)
				self.fellows.append({'name': name, 'id': id})
				msg = self.allocate_office(name)
				msgs = ''
				if accomodation == 'Y':
					msgs = self.allocate_living(name)
				return "Fellow added successfully with id " + str(id) + ". " + msg + ". " + msgs

			elif category == "staff":
				person = Staff(name, accomodation)
				if accomodation == "Y":
					return "Sorry! staff can't be accomodated" 
				else:
					self.staffs.append({'name': name, 'id': id})
					msg = self.allocate_office(name)
					return "Staff added successfully with " + str(id) + ". " + msg
		else:
			return "Wrong category. Can only be fellow or staff"

	def allocate_office(self, name):
		""" Allocates office to person added """
		if len(self.offices) > 0:
			room = randint(0, len(self.offices)-1)
			office_allocate = self.offices[room]
			if len(office_allocate['occupants']) < office_allocate['room_capacity']:
				office_allocate['occupants'].append(name)
				return "Allocated " + name + " to " + office_allocate['room_name'] + " office"
			else:
				return "No offices with space"
		else:
			return "No available offices"

	def allocate_living(self, name):
		""" Allocates living space to fellow added """
		if len(self.livingSpaces) > 0:
			room = randint(0, len(self.livingSpaces)-1)
			living_allocate = self.livingSpaces[room]
			if len(living_allocate['occupants']) < living_allocate['room_capacity']:
				living_allocate['occupants'].append(name)
				return "Allocated " + name + " to " + living_allocate['room_name'] + " Living space"
			else:
				return "No Living rooms with space"
		else:
			return "No available living rooms"