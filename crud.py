'''CRUD operations'''

from model import db, Student, Sport, Position, Location, connect_to_db

def create_student_user(student_email, 
                        student_password,
                        fname,
                        lname, 
                        gender,
                        height,
                        weight,
                        sport_name,
                        # position_id and location_id commented out for testing
                        # since the models don't exist yet
                        # position_id,
                        # location_id,
                        bio):
    '''Create and return a new student user'''

    student = Student(student_email=student_email,
                      student_password=student_password,
                      fname=fname,
                      lname=lname,
                      gender=gender,
                      height=height,
                      weight=weight,
                      sport_name=sport_name,
                    #   position_id and location_id commented out for testing  
                    #   position_id=position_id,
                    #   location_id=location_id,
                      bio=bio)
    
    return student

if __name__ == '__main__':
    from server import app
    connect_to_db(app)