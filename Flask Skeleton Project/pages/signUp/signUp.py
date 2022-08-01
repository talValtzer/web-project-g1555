from flask import Blueprint, render_template, request, session, redirect, url_for
from utilities.models.workoutsModel import workoutsModel
from utilities.models.userModel import userModel

# main_menu blueprint definition
signUp = Blueprint('signUp',__name__, static_folder='static', static_url_path='/signUp', template_folder='templates')


@signUp.route('/newUser',methods=['POST'])
def index():
    First_Name = request.form["First Name"]
    Last_Name = request.form["Last Name"]
    Email = request.form["Email"]
    User_Name = request.form["User Name"]
    Password = request.form["Password"]
    Gender = request.form["Gender"]
    Academic = request.form["Academic"]
    City = request.form["City"]
    About_Me = request.form["About Me"]
    Age = request.form["Age"]

    if len(list(userModel.userExists(User_Name))):
        return render_template("logIn.html", msg="User name already exists!")
    else :
        result = userModel.insertUser(User_Name,First_Name,Last_Name,Email,Age,Academic,Gender,City,About_Me,Password)
    return render_template('logIn.html')


@signUp.route('/signUp')
def redirect_signUp():
    return render_template('signUp.html')