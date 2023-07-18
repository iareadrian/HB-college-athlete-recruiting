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


@app.route('/users', methods=['POST'])
def register_student_user():
    '''Create a new student user'''

    email = request.form.get('email')
    password = request.form.get('password')

    student_user = crud.get_student_by_email(email)
    if student_user:
        flash('An account with that email already exists. Try again.')
    else:
        student_user = crud.create_student_user(email, password)
        db.session.add(student_user)
        db.session.commit()
        flash('Success! Please log in.')

    return redirect('/')




if __name__ == '__main__':
    connect_to_db(app)
    app.run(host='0.0.0.0', debug=True)