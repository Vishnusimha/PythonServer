from flask import Flask

from models import db
from routes import quotes_bp

def create_app():
    app = Flask(__name__)

    # Configure SQLite database
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///quotes.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    
    # Initialize database
    db.init_app(app)

    # Register blueprints
    app.register_blueprint(quotes_bp)

    return app
