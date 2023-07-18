'''CRUD operations'''

from model import db, Student, Sport, Position, Location, connect_to_db

def create_student_user(student_email,
                        student_password,
                        fname,
                        lname,
                        gender,
                        height,
                        weight,
                        bio,
                        sport_name=None,
                        position_id = None,
                        location_id=None):
    '''Create and return a new student user'''

    student = Student(student_email=student_email,
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

    sport = Sport(sport_name=sport_name)

    return sport

def create_position(position_name, sport_name=None):
    '''Create and return a new positon'''

    position = Position(position_name=position_name, sport_name=sport_name)

    return position


def create_location(city, state):
    '''Create and return a new city and state'''

    location = Location(city=city, state=state)

    return location


def get_student_by_email(student_email):
    '''Return a student user by email'''

    return Student.query.filter(Student.student_email == student_email).first()


def create_student_login(student_email, student_password):
    '''Create and return new student login credentials'''

    student_login = Student(student_email=student_email,
                            student_password=student_password)

    return student_login


if __name__ == '__main__':
    from server import app
    connect_to_db(app)