from flask import Blueprint, render_template, redirect, url_for, flash, request
from flask_login import login_required, current_user
from app import db
from app.models import Job, Application, User
from app.forms import JobForm, ApplicationForm, SearchForm

bp = Blueprint('jobs', __name__)

@bp.route('/')
def index():
    jobs = Job.query.order_by(Job.posted_at.desc()).limit(6).all()
    return render_template('jobs/index.html', jobs=jobs)

@bp.route('/search', methods=['GET', 'POST'])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        query = Job.query
        if form.keyword.data:
            query = query.filter(Job.title.ilike(f'%{form.keyword.data}%') | 
                     query.filter(Job.description.ilike(f'%{form.keyword.data}%'))
        if form.location.data:
            query = query.filter(Job.location.ilike(f'%{form.location.data}%'))
        if form.category.data:
            query = query.filter(Job.category == form.category.data)
        
        jobs = query.order_by(Job.posted_at.desc()).all()
        return render_template('jobs/search.html', form=form, jobs=jobs)
    return render_template('jobs/search.html', form=form)

@bp.route('/job/<int:job_id>')
def details(job_id):
    job = Job.query.get_or_404(job_id)
    return render_template('jobs/details.html', job=job)

@bp.route('/post', methods=['GET', 'POST'])
@login_required
def post():
    if current_user.role != 'employer':
        flash('Only employers can post jobs', 'warning')
        return redirect(url_for('jobs.index'))
    
    form = JobForm()
    if form.validate_on_submit():
        job = Job(
            title=form.title.data,
            description=form.description.data,
            requirements=form.requirements.data,
            location=form.location.data,
            salary=form.salary.data,
            category=form.category.data,
            employer_id=current_user.id
        )
        db.session.add(job)
        db.session.commit()
        flash('Your job has been posted!', 'success')
        return redirect(url_for('jobs.details', job_id=job.id))
    return render_template('jobs/post.html', form=form)

@bp.route('/apply/<int:job_id>', methods=['GET', 'POST'])
@login_required
def apply(job_id):
    if current_user.role != 'job_seeker':
        flash('Only job seekers can apply for jobs', 'warning')
        return redirect(url_for('jobs.index'))
    
    job = Job.query.get_or_404(job_id)
    form = ApplicationForm()
    
    if form.validate_on_submit():
        application = Application(
            cover_letter=form.cover_letter.data,
            job_seeker_id=current_user.id,
            job_id=job.id
        )
        db.session.add(application)
        db.session.commit()
        flash('Your application has been submitted!', 'success')
        return redirect(url_for('jobs.details', job_id=job.id))
    
    return render_template('jobs/apply.html', form=form, job=job)