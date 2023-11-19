#!/usr/bin/python3
""" Module of base class of mapping ans State class """

from sqlalchemy import Column, Integer, String, create_engine
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """Class representing base of States"""

    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)

    def __repr__(self):
        return f"<State {self.id}: {self.name}>"
