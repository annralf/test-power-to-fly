from flask_seeder import Seeder, Faker, generator
from api.models.users import User

class DemoSeeder(Seeder):
    def run(self):
        print("Getting data..")
        faker = Faker(
            cls=User,
            init={
                "user_id":1,
                "name": "Joseph",
                "lastname": "Murphy"
            }
        )

        for user in faker.create(1):
            print("Users generation %s", user)
            self.db.session.add(user)