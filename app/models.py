from datetime import datetime
from app import db, login
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    role = db.Column(db.String(20), default='job_seeker')  # 'job_seeker', 'employer', 'admin'
    company_name = db.Column(db.String(100), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    
    jobs_posted = db.relationship('Job', backref='employer', lazy='dynamic')
    applications = db.relationship('Application', backref='applicant', lazy='dynamic')

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

class Job(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)
    requirements = db.Column(db.Text)
    location = db.Column(db.String(100))
    salary = db.Column(db.String(50))
    category = db.Column(db.String(50))
    posted_at = db.Column(db.DateTime, default=datetime.utcnow)
    employer_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    
    applications = db.relationship('Application', backref='job', lazy='dynamic')

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    cover_letter = db.Column(db.Text)
    applied_at = db.Column(db.DateTime, default=datetime.utcnow)
    status = db.Column(db.String(20), default='pending')  # 'pending', 'reviewed', 'rejected', 'accepted'
    job_seeker_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    job_id = db.Column(db.Integer, db.ForeignKey('job.id'))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))