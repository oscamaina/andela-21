from sqlalchemy import Column, Integer, String, Boolean, create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

base = declarative_base()

class RoomModel(base):

	__tablename__ = 'rooms'
	room_id = Column(Integer, primary_key=True)
	room_name = Column(String(50), unique=True, nullable=False)
	room_type = Column(String(50), nullable=False)
	max_capacity = Column(Integer(), nullable=False)
	occupants = Column(Integer)


class PersonModel(base):

	__tablename__ = 'persons'
	id = Column(Integer, primary_key = True)
	name = Column(String(50), nullable=False)
	category = Column (String(50), nullable=False)
	office_allocated = Column(String, nullable=True)
	wants_accommodation = Column(Boolean)
	living_allocated = Column(String, nullable=True)
