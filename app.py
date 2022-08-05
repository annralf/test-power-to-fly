from asyncio.log import logger
from functools import cache
from gc import set_debug
from flask import Blueprint, Flask
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_caching import Cache
import logging
from flasgger  import Swagger


from api.seed.user import UserFaker

from api.services.users import ApiInit, UsersResource

from api.settings.base import Base, engine

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("api.log"), logging.StreamHandler()],
    )


bp = Blueprint('api', __name__)
db = None

@bp.cli.command('cli')
def display():
    print('cli, commands....')

@bp.cli.command('user-seed')
def settingUser():
    seedUser = UserFaker()
    return seedUser.set()

@bp.cli.command('start-database')
def starDB():
    logger.debug('starting data base')
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    logger.debug('finishing data base')

def create_app():
    app = Flask(__name__)
    Swagger(app)
    app.config.from_object("config.BaseConfig")

    cache = Cache(app)
    cache.init_app(app,config={"CACHE_TYPE": "redis"})

    db = SQLAlchemy(app)
    db.create_all()
    db.session.commit()
    Marshmallow(app)
    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    api = Api(app)
    api.add_resource(ApiInit, "/")
    api.add_resource(UsersResource, "/users/")
    
    app.register_blueprint(bp)
    return app