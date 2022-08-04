from distutils.command.build import build
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, scoped_session

import config
engine = create_engine(config.BaseConfig.SQLALCHEMY_DATABASE_URI)

Session = sessionmaker(bind=engine)
session = scoped_session(Session)

Base = declarative_base()
Base.query = session.query_property()