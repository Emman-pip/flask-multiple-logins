from flask_wtf import FlaskForm
from wtforms import PasswordField, TelField, EmailField


class UserSignup(FlaskForm):
    username = TelField('username')
    email = EmailField('email')
    password = PasswordField('password')