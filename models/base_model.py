#!/usr/bin/python3
"""This module defines a base class for all models in our hbnb clone"""
import uuid
from datetime import datetime
from sqlalchemy import Column, String, DateTime
from sqlalchemy.ext.declarative import declarative_base
from os import getenv
import models

t_fmt = "%Y-%m-%dT%H:%M:%S.%f"

Base = declarative_base()


class BaseModel:
    """A base class for all hbnb models"""
    id = Column(String(60), nullable=False, primary_key=True)
    created_at = Column(DateTime, nullable=False, default=datetime.utcnow())
    updated_at = Column(DateTime, nullable=False, default=datetime.utcnow())

    def __init__(self, *args, **kwargs):
        """Instatntiates a new model"""
        self.id = str(uuid.uuid4())
        self.created_at = datetime.now()
        self.updated_at = self.created_at
        if len(kwargs) == 0:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
        else:
            if kwargs.get("created_at"):
                kwargs["created_at"] = datetime.strptime(
                    kwargs["created_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.created_at = datetime.now()
            if kwargs.get("created_at"):
                kwargs["updated_at"] = datetime.strptime(
                    kwargs["updated_at"], "%Y-%m-%dT%H:%M:%S.%f")
            else:
                self.updated_at = datetime.now()
            for key, val in kwargs.items():
                if "__class__" not in key:
                    setattr(self, key, val)
            if not self.id:
                self.id = str(uuid.uuid4())

        '''for key, value in kwargs.items():
            if key == '__class__':
                continue
            setattr(self, key, value)
            if type(self.created_at) is str:
                self.created_at = datetime.strptime(self.created_at, t_fmt)
            if type(self.updated_at) is str:
                self.updated_at = datetime.strptime(self.updated_at, t_fmt)'''

    def __str__(self):
        """Returns a string representation of the instance"""
        return "[{:s}] ({:s}) {}".format(self.__class__.__name__, self.id,
                                         self.__dict__)

    def save(self):
        """Updates updated_at with current time when instance is changed"""
        self.updated_at = datetime.now()
        models.storage.new(self)
        models.storage.save()

    def to_dict(self, save_to_disk=False):
        """Convert instance into dict format"""
        n_dict = self.__dict__.copy()
        if "created_at" in n_dict:
            n_dict["created_at"] = n_dict["created_at"].isoformat()
        if "updated_at" in n_dict:
            n_dict["updated_at"] = n_dict["updated_at"].isoformat()
        if '_password' in n_dict:
            n_dict['password'] = n_dict['_password']
            n_dict.pop('_password', None)
        if 'amenities' in n_dict:
            n_dict.pop('amenities', None)
        if 'reviews' in n_dict:
            n_dict.pop('reviews', None)
        n_dict["__class__"] = self.__class__.__name__
        n_dict.pop('_sa_instance_state', None)
        if not save_to_disk:
            n_dict.pop('password', None)
        return n_dict

    def delete(self):
        """deletes the current instance from the storage"""
        models.storage.delete(self)
