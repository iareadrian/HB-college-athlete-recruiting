'''Script to seed the team_up database'''

import os
import crud
import model
import server

os.system('dropdb team_up')
os.system('createdb team_up')

model.connect_to_db(server.app)
model.db.create_all()

# Creating test student and coach users

basketball = crud.create_sport('basketball')
model.db.session.add(basketball)
model.db.session.commit()

point_guard = crud.create_position('point guard', basketball.sport_name)
model.db.session.add(point_guard)
model.db.session.commit()

student_city_state = crud.create_location('Oakland', 'California')
model.db.session.add(student_city_state)
model.db.session.commit()

# Create 3 test student users
for n in range(10):
    student_email = f'student_user{n}@test.com'
    student_password = 'test'
    fname = 'Chef'
    lname = 'Curry'
    gender = 'male'
    height = 75
    weight = 190
    bio = 'Chef Curry with the shot'
    sport_name = basketball.sport_name
    position = point_guard.position_id
    location = student_city_state.location_id

    student_user = crud.create_student_user(student_email, student_password, fname,
                                    lname, gender, height, weight, bio,
                                    sport_name, position, location)

    model.db.session.add(student_user)
    model.db.session.commit()

school_city_state = crud.create_location('Berkeley', 'California')
model.db.session.add(school_city_state)
model.db.session.commit()

uc_berkeley = crud.create_school('UC Berkeley', school_city_state.location_id)
model.db.session.add(uc_berkeley)
model.db.session.commit()

# Create 3 test coach users
for n in range(10):
    coach_email = f'coach_user{n}@test.com'
    coach_password = 'test'
    fname = 'Mark'
    lname = 'Fox'
    bio = "Mark Fox is the men's basketball coach at Cal"
    school_id = uc_berkeley.school_id
    school_sport = basketball.sport_name

    coach_user = crud.create_coach_user(coach_email, coach_password, fname,
                                        lname, bio, school_id, school_sport)

    model.db.session.add(coach_user)
    model.db.session.commit()
