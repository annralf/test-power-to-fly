from mmap import PAGESIZE
from cachelib import NullCache
from dotenv import load_dotenv
import os

load_dotenv(verbose=True)

cors_allowed_origins = ['*']

class ApiSetting(object):
    PAGESIZE = 2
    PAGENUMBER = 1
    SORT=False


class BaseConfig(object):
    CACHE_TYPE=os.environ['CACHE_TYPE']
    CACHE_DEFAULT_TIMEOUT=os.environ['CACHE_DEFAULT_TIMEOUT']
    CACHE_REDIS_HOST=os.environ['CACHE_REDIS_HOST']
    CACHE_REDIS_PORT=os.environ['CACHE_REDIS_PORT']
    CACHE_REDIS_DB=os.environ['CACHE_REDIS_DB']
    CACHE_REDIS_URL=os.environ['CACHE_REDIS_URL']
    CACHE_DEFAULT_TIMEOUT=os.environ['CACHE_DEFAULT_TIMEOUT']
    SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS=False


class TestBaseConfig(object):
    CACHE_TYPE=NullCache
    SQLALCHEMY_DATABASE_URI=os.environ['SQLALCHEMY_DATABASE_URI']
    SQLALCHEMY_TRACK_MODIFICATIONS=False
    TESTING=True