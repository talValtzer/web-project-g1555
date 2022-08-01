from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.models.workoutsModel import workoutsModel
from utilities.models.participantsModel import participantsModel

# main_menu blueprint definition
newWorkout = Blueprint('newWorkout', __name__, static_folder='static', static_url_path='/newWorkout',
                       template_folder='templates')


# Routes
@newWorkout.route('/newWorkout')
def index():

    return render_template('newWorkout.html')


@newWorkout.route('/createNew', methods=['POST'])
def redirect_CreateNew():
    type = request.form["type"]
    desc = request.form["Desc"]
    gender = request.form["Gender"]
    number = request.form["num_of_participants"]
    lat = request.form["lat"]
    lng = request.form["lng"]
    date = request.form["Date"]
    time = request.form["time"]
    duration = request.form["duration"]
    result = workoutsModel.insertWortkour(type, lat, lng, gender, date, time, number, session["user"],desc,duration)
    w=list(workoutsModel.lastInserted())
    w1=w[0]
    resultParticipant=participantsModel.insertParticipant(w1[0],session["user"])
    return redirect('/workouts')
