from flask import Blueprint, render_template

# Create a Blueprint for the main routes
portfolio_bp = Blueprint('portfolio', __name__)

# Define the routes
@portfolio_bp.route('/portfolio')
def index():
    return render_template('portfolio/index.html')


