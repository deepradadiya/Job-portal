from flask import Blueprint, render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import User, Job, Application

bp = Blueprint('admin', __name__)

@bp.route('/')
@login_required
def dashboard():
    if current_user.role != 'admin':
        flash('You do not have permission to access this page', 'danger')
        return redirect(url_for('jobs.index'))
    
    users_count = User.query.count()
    jobs_count = Job.query.count()
    applications_count = Application.query.count()
    
    return render_template('admin/dashboard.html', 
                         users_count=users_count,
                         jobs_count=jobs_count,
                         applications_count=applications_count)

@bp.route('/users')
@login_required
def users():
    if current_user.role != 'admin':
        flash('You do not have permission to access this page', 'danger')
        return redirect(url_for('jobs.index'))
    
    users = User.query.order_by(User.created_at.desc()).all()
    return render_template('admin/users.html', users=users)

@bp.route('/toggle_user/<int:user_id>')
@login_required
def toggle_user(user_id):
    if current_user.role != 'admin':
        flash('You do not have permission to perform this action', 'danger')
        return redirect(url_for('jobs.index'))
    
    user = User.query.get_or_404(user_id)
    if user.role == 'admin':
        flash('Cannot modify other admin accounts', 'warning')
    else:
        user.is_active = not user.is_active
        db.session.commit()
        flash(f'User {user.username} has been {"activated" if user.is_active else "deactivated"}', 'success')
    
    return redirect(url_for('admin.users'))