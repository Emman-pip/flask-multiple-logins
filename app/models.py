from sqlalchemy import Integer, String, Column, ForeignKey, Text
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

# Initialize database object
class Base(DeclarativeBase):
    pass

db = SQLAlchemy(model_class=Base)

class UserAccount(db.Model):
    user_id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    user_role = Column(String(100), nullable=False)
    
