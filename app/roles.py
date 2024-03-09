from flask import render_template, Blueprint, redirect, url_for
from flask_login import current_user, login_required

bp = Blueprint('roles', __name__)

@bp.route('/user-profile')
@login_required
def profile():
    if current_user.user_role == 'student':
        return render_template('roles/studentProfile.html', user=current_user)
    elif current_user.user_role == 'teacher':
        return render_template('roles/teacherProfile.html', user=current_user)
    return "wala"


# IMPLEMENTATION OF USER ROLES!!!
@bp.route('/student-dashboard')
@login_required
def studentDashboard():
    if current_user.user_role != 'student':
        return redirect(url_for('roles.profile'))
    
    return render_template('roles/studentDashboard.html', user=current_user)

@bp.route('/teacher-dashboard')
@login_required
def teacherDashboard():
    if current_user.user_role != 'teacher':
        return redirect(url_for('roles.profile'))
    
    return render_template('roles/teacherDashboard.html', user=current_user)