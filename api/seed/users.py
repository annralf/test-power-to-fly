from flask_seeder import Seeder, Faker, generator
from api.models.users import User

class UsersSeeder(Seeder):
    def run(self):
        print("Getting data..")
        faker = Faker(
            cls=User,
            init={
                "user_id":generator.Sequence(),
                "name": generator.Name(),
                "lastname": generator.Name()
            }
        )

        for user in faker.create(2):
            print("Users generation %s", user)
            self.db.session.add(user)