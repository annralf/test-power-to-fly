from functools import cache
from gc import set_debug
import click
from flask import Blueprint, Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_seeder import FlaskSeeder
from flask_marshmallow import Marshmallow
from flask_restful import Api
from flask_caching import Cache
import logging
from flasgger  import Swagger


from api.seed.user import UserFaker

from api.services.users import ApiInit, UsersResource

logging.basicConfig(
        level=logging.DEBUG,
        format="%(asctime)s %(name)-12s %(levelname)-8s %(message)s",
        datefmt="%m-%d %H:%M",
        handlers=[logging.FileHandler("api.log"), logging.StreamHandler()],
    )


bp = Blueprint('api', __name__)


@bp.cli.command('cli')
def display():
    print('cli, commands....')

@bp.cli.command('user-seed')
def settingUser():
    seedUser = UserFaker()
    return seedUser.set()

def create_app():
    app = Flask(__name__)
    swagger = Swagger(app)
    app.config.from_object("config.BaseConfig")

    cache = Cache(app)
    cache.init_app(app,config={"CACHE_TYPE": "redis"})

    db = SQLAlchemy(app)
    ma = Marshmallow(app)
    seeder = FlaskSeeder()
    seeder.init_app(app, db)

    api = Api(app)
    api.add_resource(ApiInit, "/")
    api.add_resource(UsersResource, "/users/")
    
    app.register_blueprint(bp)
    return app


