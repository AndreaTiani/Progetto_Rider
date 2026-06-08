from flask import Flask
from src.routes import rider_bp

def create_app():
    app = Flask(__name__)
    app.register_blueprint(rider_bp)
    return app