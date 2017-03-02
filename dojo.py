class Dojo():

	def __init__(self):
		self.rooms = []
		self.offices = []
		self.livingSpaces = []
		self.fellows = []
		self.staffs = []

	def create_room(self, room_name):
		""" function to create a unique room space """
		room_name = room_name.lower()

		if room_name in self.rooms:
			return "Room already exists"
		else:
			room_type = input("Enter room type for " + room_name + ":")
			room_type = room_type.lower()
			if room_type in ('office', 'living'):
				self.rooms.append({'room_name': room_name,'room_type': room_type})
				if room_type == 'office':
					self.offices.append({'room_name': room_name,'room_type': room_type})
					return "Office added successfully"
				elif room_type == 'living':
					self.livingSpaces.append({'room_name': room_name,'room_type': room_type})
					return "Living space added successfully"
			else:
				return "Wrong room type"
		
	def add_person(self, name, category, accomodation="N"):
		""" function to add a person """
		pass
