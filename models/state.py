#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from models.city import City
from models import storage
import os


class State(BaseModel, Base):
    """ State class """
    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", cascade="all, delete", backref="state")

    if os.getenv("HBNB_TYPE_STORAGE") == "db":
        # DBStorage
        cities = relationship("City", cascade="all, delete", backref="state")
    else:
        # FileStorage
        @property
        def cities(self):
            """Getter attribute cities"""
            city_list = []
            for city in storage.all(City).values():
                if city.state_id == self.id:
                    city_list.append(city)
            return city_list
        
    def __init__(self, *args, **kwargs):
        """Initializes the state"""
        super().__init__(*args, **kwargs)

