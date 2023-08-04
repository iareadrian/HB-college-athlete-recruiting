'''Server for college athlete recruiting app'''

from flask import Flask, render_template, request, flash, session, redirect, jsonify
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

    email = request.form.get('email')
    password = request.form.get('password')
    user_type = request.form.get('user_type')

    if user_type == 'student':
        student = crud.get_student_by_email(email)

        if not student or student.student_password != password:
            flash('The email or password you entered was incorrect. Try again.')

            return redirect('/')
        else:
            session['user_id'] = student.student_id
            session['user_type'] = 'student'
            flash('Login Successful!')

            return redirect('/student-profile')

    elif user_type == 'coach':
        coach = crud.get_coach_by_email(email)

        if not coach or coach.coach_password != password:
            flash('The email or password you entered was incorrect. Try again.')

            return redirect('/')
        else:
            session['user_id'] = coach.coach_id
            session['user_type'] = 'coach'
            flash('Login Successful!')

            return redirect('/coach-profile')


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

    coach = crud.get_coach_by_id(session['user_id'])

    coach.fname = request.form.get('fname')
    coach.lname = request.form.get('lname')
    coach.school_id = int(request.form.get('school'))
    coach.sport_name = request.form.get('sport')
    coach.bio = request.form.get('bio')

    db.session.commit()

    return redirect('/coach-profile')


@app.route('/coach-profile')
def show_coach_profile():
    '''Show coach profile'''

    coach = crud.get_coach_by_id(session['user_id'])

    return render_template('coach-profile.html', coach=coach)


@app.route('/new-search')
def show_search():
    '''Displays search page'''

    # TODO:  create routes that execute a search and display results
    user_type = session.get('user_type')

    if user_type == 'student':
        student = crud.get_student_by_id(session['user_id'])

        return render_template('search-coaches.html', student=student)

    elif user_type == 'coach':
        coach = crud.get_coach_by_id(session['user_id'])

        return render_template('search-students.html', coach=coach)


@app.route('/search', methods=['GET', 'POST'])
def run_search():
    '''Run a user search'''

    user_type = session.get('user_type')

    if user_type == 'student':
        student = crud.get_student_by_id(session['user_id'])

        fname = request.form.get('fname')
        lname = request.form.get('lname')
        school_id = int(request.form.get('school'))
        sport_name = request.form.get('sport')

        # implement search logic here

        coaches = crud.search_coaches(fname, lname, school_id, sport_name)


        return redirect('/search/results/coaches')

    # elif user_type == 'coach':
    #     coach = crud.get_coach_by_id(session['user_id'])

    #     fname = request.form.get('fname')
    #     lname = request.form.get('lname')
    #     gender = request.form.get('gender')
    #     height = request.form.get('height')
    #     weight = request.form.get('weight')
    #     sport_name = request.form.get('sport')
    #     location_id = request.form.get('location')

    #     # implement search logic here

    #     return render_template('search-students-results.html', coach=coach)


@app.route('/search/results/coaches', methods=['POST'])
def view_coach_search_results():
    '''Show search results for coach profiles'''

    student = crud.get_student_by_id(session['user_id'])

    fname = request.json.get('fname')
    lname = request.json.get('lname')
    school_id = int(request.json.get('school'))
    sport_name = request.json.get('sport')

    coaches = crud.search_coaches(fname, lname, school_id, sport_name)

    # turn coaches into a list of dictionaries
    # turn the list of dictionaries into json using jsonify
    # keys match the attributes of the coach object,
    # values match the values stored in each attribute
    print(coaches)
    search_result = []
    for coach in coaches:
        coach_dict = {
            'fname': coach.fname,
            'lname': coach.lname,
            'school_id': coach.school_name,
            'sport_name': coach.sport_name
        }
        search_result.append(coach_dict)


    return jsonify(search_result)
    # return render_template('search-coaches-results.html', studnet=student)


@app.route('/search/results/students', methods=['POST'])
def view_student_search_results():
    '''Show search results for student profiles'''

    coach = crud.get_coach_by_id(session['user_id'])

    fname = request.json.get('fname')
    lname = request.json.get('lname')
    gender = request.json.get('gender')
    height = int(request.json.get('height'))
    weight = int(request.json.get('weight'))
    sport_name = request.json.get('sport')
    position_id = int(request.json.get('position'))
    location_id = int(request.json.get('location'))



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