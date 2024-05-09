from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from app.routes.main.main import main_bp
from app.routes.portfolio.portfolio import portfolio_bp
from app.routes.blog.blog import blog_bp



# Create Flask app
app = Flask(__name__)

# Configure the database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///your_database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#register blueprints
app.register_blueprint(main_bp)
app.register_blueprint(portfolio_bp)
app.register_blueprint(blog_bp)

# Initialize the database
db = SQLAlchemy(app)