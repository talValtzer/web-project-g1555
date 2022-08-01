from flask import Blueprint, render_template, redirect, url_for, Flask
import folium
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons
import gmaps
from utilities.models.workoutsModel import workoutsModel

# main_menu blueprint definition
from app import app

homepage = Blueprint('homepage', __name__, static_folder='static', static_url_path='/homepage',
                     template_folder='templates')


# Routes


@homepage.route('/home')
def index():
    result = workoutsModel.ViewFutureWorkout2()
    return render_template('homepage.html',listworkouts=result)




@homepage.route('/homepage')
def redirect_homepage():
    return redirect(url_for('homepage.index'))
