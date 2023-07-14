'''Script to seed the team_up database'''

import os
import crud
import model
import server

os.system('dropdb team_up')
os.system('createdb team_up')

model.connect_to_db(server.app)
model.db.create_all()

# Creating only student users at this point

basketball = crud.create_sport('basketball')
model.db.session.add(basketball)
model.db.session.commit()

point_guard = crud.create_position('point guard', basketball.sport_name)
model.db.session.add(point_guard)
model.db.session.commit()

city_state = crud.create_location('Oakland', 'California')
model.db.session.add(city_state)
model.db.session.commit()

# Create 3 test student users
for n in range(3):
    student_email = f'test_user{n}@test.com'
    student_password = 'test'
    fname = 'Chef'
    lname = 'Curry'
    gender = 'male'
    height = 75
    weight = 190
    bio = 'Chef Curry with the shot'
    sport_name = basketball.sport_name
    position = point_guard.position_id
    location = city_state.location_id

    user = crud.create_student_user(student_email, student_password, fname,
                                    lname, gender, height, weight, bio,
                                    sport_name, position, location)

    model.db.session.add(user)
    model.db.session.commit()