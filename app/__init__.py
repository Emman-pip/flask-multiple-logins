from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase
import os
from dotenv import load_dotenv
from app import pages, roles
from .models import db, UserAccount
from flask_login import LoginManager

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SQLALCHEMY_DATABASE_URI"] = os.getenv('URI')
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.config["SECRET_KEY"] = os.getenv('SK')
    app.register_blueprint(pages.bp)
    app.register_blueprint(roles.bp)
    
    login_manager = LoginManager()
    login_manager.login_view = 'pages.signin'
    login_manager.init_app(app)
    
    @login_manager.user_loader
    def load_user(user_id):
        return UserAccount.query.get(user_id)
    
    db.init_app(app)
        
    return app