from flask import render_template, Blueprint
from flask_login import current_user, login_required

bp = Blueprint('roles', __name__)

@bp.route('/user-profile')
@login_required
def profile():
    if current_user.user_role == 'student':
        return render_template('pages/studentProfile.html', user=current_user)
    elif current_user.user_role == 'teacher':
        return render_template('pages/teacherProfile.html', user=current_user)
    return "wala"