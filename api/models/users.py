from unicodedata import name
from pkg_resources import declare_namespace
from sqlalchemy import Column, Integer, String, Table

from sqlalchemy.ext.declarative import declarative_base
from api.settings.base import Base

class User(Base):
    __tablename__ = "user_api"
    user_id = Column(Integer, primary_key=True)
    name = Column(String)
    lastname = Column(String)

    def __init__(self, user_id, name, lastname):
        self.user_id = user_id
        self.name = name
        self.lastname = lastname

    def __str__(self):
        return "user_id=%d, name=%s, lastname=%s" % (self.user_id, self.name, self.lastname)