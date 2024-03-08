from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv
from app import pages
from .models import db


load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv('SK')
    app.register_blueprint(pages.bp)
    
    db.init_app(app)
        
    return app