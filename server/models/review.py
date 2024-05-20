#!/usr/bin/python3
""" Review module """
from server.models.base_model import BaseModel, Base
from sqlalchemy import Column, String, ForeignKey


class Review(BaseModel, Base):
    """Representation of Review """

    __tablename__ = 'reviews'
    gym_id = Column(String(60), ForeignKey('gymes.id'), nullable=False)
    client_id = Column(String(60), ForeignKey('clients.id'), nullable=False)
    text = Column(String(1024), nullable=False)

    def __init__(self, *args, **kwargs):
        """initializes Review"""
        super().__init__(*args, **kwargs)
