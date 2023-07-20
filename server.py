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
        flash('Success!')

        return redirect('/complete-student-profile')


@app.route('/complete-student-profile')
def complete_profile():
    '''Finish creating a student profile'''

    return render_template('complete-student-profile.html')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)