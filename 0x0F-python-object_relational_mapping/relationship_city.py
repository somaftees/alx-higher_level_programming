#!/usr/bin/python3
"""
a script that creates the State “California” with..."""

from relationship_state import Base, State
from sqlalchemy import Column, Integer, String, ForeignKey


class City(Base):
    """City class"""
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'), nullable=False)
