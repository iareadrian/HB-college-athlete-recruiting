'''Server for college athlete recruiting app'''

from flask import Flask, render_template, request, flash, session, redirect
from jinja2 import StrictUndefined
from model import connect_to_db, db
import crud
import os

app = Flask(__name__)
app.secret_key = os.environ['FLASK_SECRET_KEY']
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    '''View the home page'''

    return render_template('homepage.html')


@app.route('/login', methods=['POST'])
def login_user():
    '''Log users in'''

# TODO: finish login route


@app.route('/register/student', methods=['POST'])
def register_student_user():
    '''Create a new student user'''

    email = request.form.get('email')
    password = request.form.get('password')

    student_user = crud.get_student_by_email(email)
    if student_user:
        flash('An account with that email already exists. Try again.')

        return redirect('/')
    else:
        student_user = crud.create_student_login(email, password)
        db.session.add(student_user)
        db.session.commit()
        session['user_id'] = student_user.student_id
        session['user_type'] = 'student'
        flash('Success!')

        return redirect('/complete-student-profile')


@app.route('/register/coach', methods=['POST'])
def register_coach_user():
    '''Create a new coach user'''

    email = request.form.get('email')
    password = request.form.get('password')

    coach_user = crud.get_coach_by_email(email)
    if coach_user:
        flash('An account with that email already exists. Try again.')

        return redirect('/')
    else:
        coach_user = crud.create_coach_login(email, password)
        db.session.add(coach_user)
        db.session.commit()
        session['user_id'] = coach_user.coach_id
        session['user_type'] = 'coach'
        flash('Success!')

        return redirect('/complete-coach-profile')


@app.route('/complete-student-profile')
def show_student_form():
    '''Shows the student profile completion form'''


    return render_template('complete-student-profile.html')


@app.route('/complete-student-profile', methods=['POST'])
def finish_student_profile():
    '''Creates a student profile after registration'''

    student = crud.get_student_by_id(session['user_id'])
    print(student)

    student.fname = request.form.get('fname')
    student.lname = request.form.get('lname')
    student.gender = request.form.get('gender')
    student.height = int(request.form.get('height'))
    student.weight = int(request.form.get('weight'))

    # Make dropdown menu for things that are already seeded in the db
    student.sport_name = request.form.get('sport')
    student.position_id = int(request.form.get('position'))
    student.location_id = int(request.form.get('location'))

    # 2.0 allow users to type a location

    student.bio = request.form.get('bio')

    db.session.commit()
    print('****************************')
    print(student)

    return redirect('/student-profile')


@app.route('/student-profile')
def show_student_profile():
    '''Show student profile'''

    # pull student info from student in session

    student = crud.get_student_by_id(session['user_id'])

    return render_template('student-profile.html', student=student)


@app.route('/complete-coach-profile')
def show_coach_form():
    '''Shows the coach profile completion form'''

    return render_template('complete-coach-profile.html')


@app.route('/complete-coach-profile', methods=['POST'])
def finish_coach_profile():
    '''Creates a coach profile after registration'''


    return redirect('/coach-profile')


@app.route('/coach-profile')
def show_coach_profile():
    '''Show coach profile'''

    return render_template('coach-profile.html')


@app.route('/logout', methods=['POST'])
def user_logout():
    '''Log users out'''

    user_type = session.get('user_type')

    if user_type == 'student':
        session.pop('student', None)
    flash('You have successfully logged out')

    return redirect('/')


if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)