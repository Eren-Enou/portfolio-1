from flask import Blueprint, render_template

# Create a Blueprint for the main routes
main_bp = Blueprint('main', __name__)

# Define the routes
@main_bp.route('/')
def index():
    return render_template('main/index.html')

@main_bp.route('/about')
def about():
    return render_template('main/about.html')

@main_bp.route('/contact')
def contact():
    return render_template('main/contact.html')




# You can define more routes for the main section here

# You may also include additional imports and functions related to the main routes if needed
