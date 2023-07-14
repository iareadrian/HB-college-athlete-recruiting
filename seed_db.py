'''Script to seed the team_up database'''

import os
import crud
import model
import server

os.system('dropdb team_up')
os.system('createdb team_up')

model.connect_to_db(server.app)
model.db.create_all()

basketball = crud.create_sport('basketball')
model.db.session.add(basketball)

point_guard = crud.create_position('point guard', basketball)
model.db.session.add(point_guard)

for n in range(3):
    student_email = f'test_user{n}@test.com'
    student_password = 'test'
    fname = 'Chef'
    lname = 'Curry'
    gender = 'male'
    height = 75
    weight = 190
    bio = 'Chef Curry with the shot'
    sport_name = basketball
    position = 1
    location = 1

    # TODO finish creating test data