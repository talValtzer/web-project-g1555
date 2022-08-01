from flask import Blueprint, render_template

# main_menu blueprint definition
conditions = Blueprint('conditions', __name__, static_folder='static', static_url_path='/conditions', template_folder='templates')

# Routes


@conditions.route('/conditions')
def redirect_conditions():
     return render_template('conditions.html')
