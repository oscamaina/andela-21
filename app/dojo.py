import os
from random import choice

from app.rooms import Room, Office, LivingSpace
from app.person import Person, Fellow, Staff
from app.db_models import RoomModel, PersonModel, base

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.sql import select

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
		name = (first_name + " " + last_name).upper()
		if not any(char.isdigit() for char in name):
			if category.lower() == "fellow":
				person = Fellow(name, accomodation)
				person.person_id  = first_name[0].upper() + last_name[0].upper()\
				 + str(int(len(self.all_people)+1))
				self.fellows.append(person)
				self.all_people.append(person)
				self.waiting_to_allocate_office.append(person)
				if accomodation.upper() == 'Y':
					self.waiting_to_allocate_living.append(person)
					return "Fellow " + person.name + " added successfully with id " \
					 + person.person_id + ", " + str(self.allocate_office(person)) \
					 + " and " + str(self.allocate_living(person))
				return "Fellow " + person.name\
				 + " added successfully with id " + person.person_id + " and " \
				+ str(self.allocate_office(person))

			elif category.lower() == "staff":
				if accomodation.upper() == "Y":
					return "Sorry! staff can't be accomodated"
				else:
					person = Staff(name)
					person.person_id  = first_name[0].upper() + last_name[0].upper()\
					 + str(int(len(self.all_people)+1))
					self.staffs.append(person)
					self.all_people.append(person)
					self.waiting_to_allocate_office.append(person)
					return "Staff " + person.name + " added successfully with id " \
					+ person.person_id + " and " + str(self.allocate_office(person))
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
		if office_with_space:
			random_office = choice(office_with_space)
			random_office.occupants.append(person.name)
			person.office = random_office.room_name
			self.waiting_to_allocate_office.remove(person)
			return "allocated to " + random_office.room_name + " Office space"
		else:
			return "No offices with space available"

	def allocate_living(self, person):
		""" Allocates living space to fellow added """

		living_with_space = []
		#filters living_spaces and returns ones with space
		for living_allocate in self.living_spaces:
			if len(living_allocate.occupants) < living_allocate.max_capacity:
				living_with_space.append(living_allocate)
		if living_with_space:
			random_living_space = choice(living_with_space)
			random_living_space.occupants.append(person.name)
			person.living = random_living_space.room_name
			self.waiting_to_allocate_living.remove(person)
			return "allocated to " + random_living_space.room_name + \
			" Living space"
		else:
			return "No living rooms with space available"

	def print_room(self, room_name):
		""" Returns all occupants of a specific room """
		found = False
		current_occupants = ""
		for room in self.all_rooms:
			if room.room_name == room_name.lower():
				found = True
			if found:
				if len(room.occupants) > 0:
					for occupant in room.occupants:
						current_occupants += " {},".format(occupant)
					current_occupants = current_occupants[:-1]
					return current_occupants
				else:
					return room_name + " has no occupants"
		else:
			return "Room " + room_name + " doesn't exist"

	def print_allocations(self, filename=None):
		""" Returns rooms occupied with there current occupants """
		output = ""
		#filters all_rooms to return room with occupants
		room_with_occupants = [room for room in self.all_rooms \
		if room.occupants]

		if room_with_occupants:
			for room in room_with_occupants:
				output += ("\n ROOM {} {}".format\
				(room.room_name.upper(), room.room_type.upper()))
				output += ("\n" + "-"*50 + "\n")
				for occupant in room.occupants:
					output += (" {},".format(occupant))
				output = output[:-1]
				output += "\n"

			if filename is None:
				return output

			else:
				txt_file = open(filename + ".txt", "w")
				txt_file.write(output)
				txt_file.close()
				return("Data saved in {}.txt".format(filename) )
		return "No allocations availabe"

	def print_unallocated(self, filename=None):
		""" Returns all persons yet to be allocated rooms """
		output = ''
		if self.waiting_to_allocate_office:
			output += "\nPersons yet to be allocated office space\n" + "-"*40
			output += ("\nID" + " "*5 + "NAME" + " "*10 + "CATEGORY")
			for person in self.waiting_to_allocate_office:
				if person.category == 'fellow':
					output += ("\n{} {}     {}". \
					format(person.person_id, person.name, person.category))

				elif person.category == 'staff':
					output += ("\n{} {}      {}".format\
					(person.person_id, person.name, person.category))
		else:
			output += "\n There are no unallocated persons in office \n"
		output += "\n"

		if self.waiting_to_allocate_living:
			output += "\nPersons yet to be allocated living rooms\n" + "-"*40
			output += ("\nID" + " "*5 + "NAME")
			for person in self.waiting_to_allocate_living:
				output += ("\n {} {}".format(person.person_id, person.name))
		else:
			output += "\n There are no unallocated persons in living"

		if filename is None:
			return(output)

		else:
			txt_file = open(filename + ".txt", "w")
			txt_file.write(output)
			txt_file.close()
			return("Data saved in {}.txt".format(filename) )

	def reallocate_person(self, personID, roomname):
		""" Reallocates person to a different room """
		#returns rooms with occupants
		room_with_occupants = [room for room in self.all_rooms \
		if room.occupants]

		person_reallocate = [person for person \
		in self.all_people if person.person_id == personID.upper()]

		if not person_reallocate:
			return "The person with id " + str(personID) + " doesn't exist"
		#checks if person is in allocated a room
		previous_room = [room for room in room_with_occupants\
		 for occupant in room.occupants if occupant.upper() ==\
		  person_reallocate[0].name]

		if not previous_room:
			return "person yet to be allocated a room"

		#checks if room to rellocate to exists
		new_room = [room for room in self.all_rooms \
		if room.room_name.lower() == roomname.lower()]

		if not new_room:
			return "room " + roomname + " doesn't exists"
		if new_room:
			#checks if previous room type matches with new room type
			roomtypes = [oldroom for oldroom in \
			previous_room if oldroom.room_type == new_room[0].room_type]
		if person_reallocate[0].category == "staff" \
		and new_room[0].room_type == "living":
			return "Can't rellocate staff to a living room"
		if not roomtypes:
			return "can't rellocate to a room of different type"
		if new_room[0] in previous_room:
			return "Can't reallocate to the same room"
			#checks if room to rellocate to has space
		if len(new_room[0].occupants) == new_room[0].max_capacity:
			return "Sorry, room " + new_room[0].room_name.capitalize() + " is full"
		else:
			if new_room[0].room_type == previous_room[0].room_type:
				new_room[0].occupants.append(person_reallocate[0].name)
				previous_room[0].occupants.remove(person_reallocate[0].name)
			else:
				new_room[0].occupants.append(person_reallocate[0].name)
				previous_room[1].occupants.remove(person_reallocate[0].name)
			return person_reallocate[0].name + " " + "reallocated to " + roomname

	def load_people(self, filename):
		""" Loads people from a file to system """
		response = ""
		if not os.path.isfile(filename):
			return "File {} doesn't exist".format(filename)
		text_file = open(filename)
		if os.path.getsize(filename) == 0:
			response += "File {} is empty".format(filename)
		for line in text_file:
			person_details = line.rstrip().split()
			if len(person_details) == 4 and person_details[2] \
			in ("FELLOW", "STAFF") and person_details[3] in ("Y", "N"):
				response += str(self.add_person(person_details[0], person_details[1], \
				person_details[2], person_details[3])) + "\n\n"
			elif len(person_details) == 3 and person_details[2] in \
			("FELLOW", "STAFF"):
				response += str(self.add_person(person_details[0], \
				person_details[1], person_details[2])) + "\n\n"
			else:
				response += "Incorrect data format for -- {0}".format(line)
		return response

	def save_state(self, dbname="dojo"):
		"""persists application data to database"""

		engine = create_engine('sqlite:///database/{}.db'.format(dbname))
		base.metadata.create_all(engine)
		Session = sessionmaker(bind=engine)
		session = Session()

		for room in self.all_rooms:
		    new_room = RoomModel(
		        room_name=room.room_name, \
		        room_type=room.room_type, \
		        max_capacity=room.max_capacity, \
				occupants = ",".join(room.occupants)
		    )
		    room_exists = session.query(RoomModel).filter\
			(RoomModel.room_name == room.room_name).count()
		    if not room_exists:
		        session.add(new_room)
		session.commit()

		for person in self.all_people:
			if person.category == 'staff':
				accomodation = "N"
			else:
				accomodation = "Y" if person.accomodation.upper() == 'Y' else "N"

			new_person = PersonModel(person_id = person.person_id, name = person.name, \
			category = person.category, office_allocated = person.office,\
			wants_accomodation = accomodation,\
			living_allocated = person.living)
			person_exists = session.query(PersonModel).filter\
			(PersonModel.person_id == person.person_id).count()
			if not person_exists:
				session.add(new_person)
		session.commit()
		return "App data has been stored in {} database".format(dbname)

	def load_state(self, dbname):
		""" Loads data to application from a database """

		if not os.path.isfile("./database/{}.db".format(dbname)):
			return dbname + " does not exist"

		engine = create_engine('sqlite:///database/{}.db'.format(dbname))
		Session = sessionmaker(bind=engine)
		session = Session()

		rooms = session.query(RoomModel).all()
		persons = session.query(PersonModel).all()

		self.all_rooms = []
		self.waiting_to_allocate_living = []
		self.waiting_to_allocate_office = []
		for room in rooms:
			if room.room_type == 'office':
				office = Office(room.room_name)
				office.occupants = room.occupants.split(",")
				self.all_rooms.append(office)
				self.offices.append(office)
			elif room.room_type == 'living':
				living = LivingSpace(room.room_name)
				living.occupants = room.occupants.split(",")
				self.all_rooms.append(living)
				self.living_spaces.append(living)

		self.all_people = []
		for person in persons:
			if person.category == 'staff':
				staff = Staff(person.name)
				staff.office = person.office_allocated
				staff.person_id = person.person_id
				self.all_people.append(staff)
				self.staffs.append(staff)

			elif person.category == 'fellow':
				fellow = Fellow(person.name, person.wants_accomodation)
				fellow.office = person.office_allocated
				fellow.living = person.living_allocated
				fellow.person_id = person.person_id
				self.all_people.append(fellow)
				self.fellows.append(fellow)
				if not person.living_allocated:
					self.waiting_to_allocate_living.append(person)
			if not person.office_allocated:
				self.waiting_to_allocate_office.append(person)
		return "successfully loaded"
