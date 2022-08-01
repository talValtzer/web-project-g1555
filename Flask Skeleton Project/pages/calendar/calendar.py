from flask import Blueprint, render_template,session
from utilities.models.workoutsModel import workoutsModel
# main_menu blueprint definition
calendar = Blueprint('calendar', __name__, static_folder='static', static_url_path='/calendar', template_folder='templates')


# Routes
@calendar.route('/calendar')
def redirect_workouts():
     return render_template('calendar.html')

@calendar.route('/calendar2')
def redirect_workouts2():
     print((session["user"]))
     cw = list(workoutsModel.ViewCallendar(session["user"]))
     print(cw)

     return render_template('calendar2.html',events=cw)
