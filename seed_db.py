'''Script to seed the team_up database'''

from faker import Faker
import random
import os
import crud
import model
import server

fake = Faker()

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

curry_email = 'chef_curry@test.com'
curry_password = 'test'
curry_fname = 'Chef'
curry_lname = 'Curry'
curry_gender = 'male'
curry_height = 75
curry_weight = 190
curry_bio = 'Chef Curry with the shot'
curry_sport_name = basketball.sport_name
curry_position = point_guard.position_id
curry_location = student_city_state.location_id

chef_curry = crud.create_student_user(curry_email, curry_password, curry_fname,
                                    curry_lname, curry_gender, curry_height, curry_weight, curry_bio,
                                    curry_sport_name, curry_position, curry_location)

model.db.session.add(chef_curry)
model.db.session.commit()

# Create 10 test student users
for n in range(10):
    student_email = f'student_user{n}@test.com'
    student_password = 'test'
    fname = fake.first_name()
    lname = fake.last_name()
    random_gender = random.choice(['male', 'female'])
    random_height = random.randint(60, 80)
    random_weight = random.randint(120, 230)
    bio = f'Hello, my name is {fname} {lname}. Ready to put in work!'
    sport_name = basketball.sport_name
    position = point_guard.position_id
    location = student_city_state.location_id

    student_user = crud.create_student_user(student_email, student_password, fname,
                                    lname, random_gender, random_height, random_weight, bio,
                                    sport_name, position, location)

    model.db.session.add(student_user)
    model.db.session.commit()

school_city_state = crud.create_location('Berkeley', 'California')
model.db.session.add(school_city_state)
model.db.session.commit()

uc_berkeley = crud.create_school('UC Berkeley', school_city_state.location_id)
model.db.session.add(uc_berkeley)
model.db.session.commit()

fox_email = 'mark_fox@test.com'
fox_password = 'test'
fox_fname = 'Mark'
fox_lname = 'Fox'
fox_bio = "Mark Fox is the men's basketball coach at Cal"
fox_school_id = uc_berkeley.school_id
fox_school_sport = basketball.sport_name

mark_fox = crud.create_coach_user(fox_email, fox_password, fox_fname,
                                        fox_lname, fox_bio, fox_school_id, fox_school_sport)

model.db.session.add(mark_fox)
model.db.session.commit()

# Create 10 test coach users
for n in range(10):
    coach_email = f'coach_user{n}@test.com'
    coach_password = 'test'
    fname = fake.first_name()
    lname = fake.last_name()
    bio = f"Hello, I'm Coach {fname} {lname}. We're taking the ship!"
    school_id = uc_berkeley.school_id
    school_sport = basketball.sport_name

    coach_user = crud.create_coach_user(coach_email, coach_password, fname,
                                        lname, bio, school_id, school_sport)

    model.db.session.add(coach_user)
    model.db.session.commit()
