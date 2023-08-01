'''CRUD operations'''

import model


def create_student_user(student_email,
                        student_password,
                        fname,
                        lname,
                        gender,
                        height,
                        weight,
                        bio,
                        sport_name=None,
                        position_id=None,
                        location_id=None):
    '''Create and return a new student user'''

    student = model.Student(student_email=student_email,
                      student_password=student_password,
                      fname=fname,
                      lname=lname,
                      gender=gender,
                      height=height,
                      weight=weight,
                      bio=bio,
                      sport_name=sport_name,
                      position_id=position_id,
                      location_id=location_id)
    return student


def create_sport(sport_name):
    '''Create and return a new sport'''

    sport = model.Sport(sport_name=sport_name)

    return sport


def create_position(position_name, sport_name=None):
    '''Create and return a new positon'''

    position = model.Position(position_name=position_name, sport_name=sport_name)

    return position


def create_location(city, state):
    '''Create and return a new city and state'''

    location = model.Location(city=city, state=state)

    return location


def get_student_by_email(student_email):
    '''Return a student user by email'''

    return model.Student.query.filter(model.Student.student_email == student_email).first()


def get_student_by_id(student_id):
    '''Get a student by student id'''

    return model.Student.query.get(student_id)


def create_student_login(student_email, student_password):
    '''Create and return new student login credentials'''

    student_login = model.Student(student_email=student_email,
                            student_password=student_password)

    return student_login


def create_coach_user(coach_email,
                      coach_password,
                      fname,
                      lname,
                      bio,
                      school_id=None,
                      sport_name=None):
    '''Create and return a new coach user'''

    coach = model.Coach(coach_email=coach_email,
                        coach_password=coach_password,
                        fname=fname,
                        lname=lname,
                        bio=bio,
                        school_id=school_id,
                        sport_name=sport_name)

    return coach


def get_coach_by_id(coach_id):
    '''Get a coach user by coach id'''

    return model.Coach.query.get(coach_id)


def get_coach_by_email(coach_email):
    '''Return a coach user by email'''

    return model.Coach.query.filter(model.Coach.coach_email == coach_email).first()


def create_coach_login(coach_email, coach_password):
    '''Create and return new coach login credentials'''

    coach_login = model.Coach(coach_email=coach_email,
                            coach_password=coach_password)

    return coach_login


def search_coaches(fname=None, lname=None, school_id=None, sport_name=None):
    '''Search for coaches'''

    # FIXME: This query assumes all search fields will be filled in
    # Separate, then chain queries together so users don't have to enter every field
    coaches = model.Coach.query.filter(model.Coach.fname == fname,
                                       model.Coach.lname == lname,
                                       model.Coach.school_id == school_id,
                                       model.Coach.sport_name == sport_name).all()

    print("Received search parameters:")
    print("fname:", fname)
    print("lname:", lname)
    print("school_id:", school_id)
    print("sport_name:", sport_name)

    return coaches


def create_school(school_name, location_id=None):
    '''Create and return a new school'''

    school = model.School(school_name=school_name, location_id=location_id)

    return school


if __name__ == '__main__':
    from server import app
    model.connect_to_db(app)


'''if the values for all the fields are empty, show no results
otherwise chain queries
first select all coaches
if a value has been provided to the first name field
take the query, and add the chain
if the field last name, has a value
take the query, add it to the chain
...
execute the query at the end .all()
gets the result that we can pass forward'''