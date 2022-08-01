from flask import Flask
from flask_googlemaps import GoogleMaps
from flask_googlemaps import Map, icons

###### App setup
app = Flask(__name__)
app.config.from_pyfile('settings.py')



###### Pages


## Conditions
from pages.conditions.conditions import conditions
app.register_blueprint(conditions)

## search
from pages.search.search import search
app.register_blueprint(search)

## homepage
from pages.homepage.homepage import homepage
app.register_blueprint(homepage)

## myProfile
from pages.myProfile.myProfile import myProfile
app.register_blueprint(myProfile)

##Workouts
from pages.workouts.workouts import workouts
app.register_blueprint(workouts)

## new workout
from pages.newWorkout.newWorkout import newWorkout
app.register_blueprint(newWorkout)

## calendar
from pages.calendar.calendar import calendar
app.register_blueprint(calendar)

#############


##contact us page
from pages.contactUs.contactUs import contactUs
app.register_blueprint(contactUs)

## Page error handlers
from pages.page_error_handlers.page_error_handlers import page_error_handlers
app.register_blueprint(page_error_handlers)

## Login
from pages.logIn.logIn import logIn
app.register_blueprint(logIn)

##sighUp
from pages.signUp.signUp import signUp
app.register_blueprint(signUp)

##workoutDetails
from pages.workoutDetails.workoutDetails import workoutDetails
app.register_blueprint(workoutDetails)




###### Components
## navbar
from components.navBar.navBar import navBar
app.register_blueprint(navBar)

## footer
from components.footer.footer import footer
app.register_blueprint(footer)

