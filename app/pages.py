from flask import Blueprint, render_template, url_for, request, flash, redirect
from .models import UserAccount
from werkzeug.security import generate_password_hash, check_password_hash
import app

bp = Blueprint('pages', __name__)


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('pages/home.html')

@bp.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        email = request.form.get('email')
        username = request.form.get('username')
        password = request.form.get('password')
        role = request.form.get('role')
        
        user = UserAccount.query.filter_by(email=email).first()
        
        if user:
            flash("You already have an account!!! Proceed to the login section.")
            return redirect(url_for('pages.signup'))

        user = UserAccount(
            email=email, 
            username=username, 
            password=generate_password_hash(password), 
            user_role=str(role)
            )
        app.db.session.add(user)
        app.db.session.commit()
        flash('You successfully signed up!')
        return redirect(url_for('pages.signup'))
    return render_template('pages/signups.html')