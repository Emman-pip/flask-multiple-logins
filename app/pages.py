from flask import Blueprint, render_template, url_for


bp = Blueprint('pages', __name__)


@bp.route('/')
@bp.route('/home')
def home():
    return render_template('pages/home.html')
