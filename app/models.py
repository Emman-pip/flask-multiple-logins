from sqlalchemy import Integer, String, Column, ForeignKey, Text
from app import db

class UserAccount(db.Model):
    user_id = Column(Integer, primary_key=True)
    username = Column(String(100), unique=True, nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    password = Column(Text, nullable=False)
    user_role = Column(String(100), nullable=False)
    
