from flask import Blueprint, render_template, session, redirect, url_for
from flask import request
from utilities.models.userModel import userModel

# main_menu blueprint definition
myProfile = Blueprint('myProfile', __name__, static_folder='static', static_url_path='/myProfile',
                      template_folder='templates')


@myProfile.route('/myProfile')
def ChangeDetails():
    user = list(userModel.ViewUserDetails(session["user"]))
    return render_template('myProfile.html', user=user[0])


@myProfile.route('/update_user', methods=["POST"])
def update_user():
    print(session['user'])
    User_name = session['user']
    First_name = request.form['firstname']
    Last_name = request.form['lastname']
    email = request.form['Email']
    Academic_institution = request.form['Academic']
    Gender = request.form['Gender']
    City = request.form['City']
    about_me = request.form['AboutMe']
    result = userModel.updateUser(User_name, First_name, Last_name, email, Academic_institution, Gender, City, about_me)
    print(result)
    return redirect(url_for("myProfile.ChangeDetails"))