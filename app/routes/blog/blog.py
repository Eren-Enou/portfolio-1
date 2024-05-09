from flask import Blueprint, render_template

# Create a Blueprint for the main routes
blog_bp = Blueprint('blog', __name__)

# Define the routes
@blog_bp.route('/blog')
def index():
    return render_template('blog/index.html')


