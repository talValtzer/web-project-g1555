from flask import Blueprint, render_template

# main_menu blueprint definition
navBar = Blueprint('navBar', __name__, static_folder='static', static_url_path='/navBar', template_folder='templates')
