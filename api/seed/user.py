from faker import Faker
from flask import session
from setuptools import find_packages
from api.settings.base import Session
from api.models.users import User


class UserFaker():
    def set(self):
        faker = Faker(['en_US'])
        users = []
        local_session = Session()
        idUser = 0
        for _ in range(1000000):
            idUser += 1
            name = faker.first_name()
            lastname = faker.last_name()
            user = User(
                user_id = idUser,
                name =  name,
                lastname = lastname
            )
            print(f'Adding user {idUser} ---- {name}')
            users.append(user)
        local_session.bulk_save_objects(users)
        local_session.commit()