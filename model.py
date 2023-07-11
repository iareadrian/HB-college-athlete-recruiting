'''Models for college athlete recruiting app'''

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Student(db.Model):
    '''Student user'''

    __tablename__ = 'students'

    student_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    student_email = db.Column(db.String(50), unique=True)
    student_password = db.Column(db.String(50))
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    gender = db.Column(db.String(20))
    height = db.Column(db.Integer)
    weight = db.Column(db.Integer)
    sport_name = db.Column(db.String(30), db.ForeignKey('sports'))
    position_id = db.Column(db.Integer, db.ForeignKey('positions'))
    city = db.Column(db.String(30))
    state = db.Column(db.String(20))
    bio = db.Column(db.String)

    # TODO: Create relationships

    def __repr__(self):
        return (
            f'<Student student_id = {self.student_id}, '
            f'student_email = {self.student_email}, '
            f'fname = {self.fname}>'
        )
    

class Coach(db.Model):
    '''Coach user'''

    __tablename__ = 'coaches'

    coach_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    coach_email = db.Column(db.String(50), unique=True)
    coach_password = db.Column(db.String(50))
    fname = db.Column(db.String(30))
    lname = db.Column(db.String(30))
    school_id = db.Column(db.Integer, db.ForeignKey('schools'))
    bio = db.Column(db.String)

    # TODO: Create relationships

    def __repr__(self):
        return (
            f'<Coach coach_id = {self.coach_id}, '
            f'coach_email = {self.coach_email}, '
            f'fname = {self.fname}>'
        )


class Sport(db.Model):
    '''Type of sport played or coached'''

    __tablename__ = 'sports'

    sport_name = db.Column(db.String(30), primary_key=True)
    sport_id = db.Column(db.Integer, autoincrement=True)

    # TODO: Create relationships

    def __repr__(self):
        return (
            f'<Sport sport_name = {self.sport_name}, '
            f'sport_id = {self.sport_id}>'
        )


class Position(db.Model):
    '''Athlete's position on the team'''

    __tablename__ = 'positions'

    position_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    position_name = db.Column(db.String(30))
    sport_name = db.Column(db.String(30), db.ForeignKey('sports'))

    # TODO: Create relationships

    def __repr__(self):
        return (
            f'<Position position_id = {self.position_id}, '
            f'position_name = {self.position_name}>'
        )


class School(db.Model):
    '''A college'''

    __tablename__ = 'schools'

    school_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    school_name = db.Column(db.String)
    city = db.Column(db.String(30))
    state = db.Column(db.String(20))

    # TODO: Create relationships

    def __repr__(self):
        return (
            f'<School school_id = {self.school_id}, '
            f'school_name = {self.school_name}>'
        ) 


class SportSchool(db.Model):
    '''Links the Sport and School classes'''

    __tablename__ = 'sports_schools'

    sportschool_id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    sport_name = db.Column(db.String(30), db.ForeignKey('sports'))
    school_id = db.Column(db.Integer, db.ForeignKey('schools'))

    # TODO: Create relationships

    def __repr__(self):
        return (
            f'<SportSchool sportschool_id = {self.sportschool_id}, '
            f'sport_name = {self.sport_name}>'
        ) 


def connect_to_db(flask_app, db_uri='postgresql:///team_up', echo=True):
    flask_app.config['SQLALCHEMY_DATABASE_URI'] = db_uri
    flask_app.config['SQLALCHEMY_ECHO'] = echo
    flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.app = flask_app
    db.init_app(flask_app)

    print('Connected to the DB')

# Allows db to be used interactively in terminal
if __name__ == '__main__':
    from server import app
    connect_to_db(app)