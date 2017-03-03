class Room(object):
	""" simulating room class """
	def __init__(self, room_name):
		""" Initializing room attributes """
		self.room_name = room_name

class Office(Room):
	""" Office class inheriting from room class"""
	def __init__(self, room_name):
		super().__init__(room_name)
		self.room_type = 'office'
		self.max_capacity = 4

class LivingSpace(Room):
	""" LivingSpace class inheriting from room class"""
	def __init__(self, room_name):
		super().__init__(room_name)
		self.room_type = 'living'
		self.max_capacity = 6