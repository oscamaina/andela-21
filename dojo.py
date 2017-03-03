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

	def create_room(self, room_type, room_name):
		""" function to create a unique room space """
		room_name = room_name.lower()
		room_type = room_type.lower()

		if room_name in self.rooms:
			return "Room already exists"
		else:
			if room_type in ('office', 'living'):
				self.rooms.append(room_name)
				if room_type == 'office':
					room = Office(room_name)
					self.offices.append(room)
					return "Office added successfully"
				elif room_type == 'living':
					room = LivingSpace(room_name)
					self.livingSpaces.append(room)
					return "Living space added successfully"
			else:
				return "Wrong room type"
	def add_person(self, name, category, accomodation="N"):
		""" function to add a person """
		pass
