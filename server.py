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
        session['student'] = student_user.student_id
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
        session['coach'] = coach_user.coach_id
        flash('Success!')

        return redirect('/complete-coach-profile')


@app.route('/complete-student-profile')
def show_student_form():
    '''Shows the student profile completion form'''

    return render_template('complete-student-profile.html')


@app.route('/complete-student-profile', methods=['POST'])
def finish_student_profile():
    '''Creates a student profile after registration'''

    # Placeholder.  Should redirect to the student profile page
    return redirect('/complete-student-profile')


@app.route('/complete-coach-profile')
def show_coach_form():
    '''Shows the coach profile completion form'''

    return render_template('complete-coach-profile.html')


@app.route('/complete-coach-profile', methods=['POST'])
def finish_coach_profile():
    '''Creates a coach profile after registration'''

    # This line is a placeholder.
    # Needs to go to the coach's profile page
    return redirect('/complete-coach-profile')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)