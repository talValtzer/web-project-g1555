from flask import Blueprint, render_template

# main_menu blueprint definition
contactUs = Blueprint('contactUs', __name__, static_folder='static', static_url_path='/contactUs', template_folder='templates')

@contactUs.route('/contactUs')
def redirect_homepage():
     return render_template('contactUs.html')
