from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextAreaField, SelectField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=2, max=64)])
    email = StringField('Email', validators=[DataRequired(), Email()])
    role = SelectField('Role', choices=[('job_seeker', 'Job Seeker'), ('employer', 'Employer')], validators=[DataRequired()])
    company_name = StringField('Company Name (for employers)', validators=[Length(max=100)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

class JobForm(FlaskForm):
    title = StringField('Job Title', validators=[DataRequired(), Length(max=100)])
    description = TextAreaField('Description', validators=[DataRequired()])
    requirements = TextAreaField('Requirements', validators=[DataRequired()])
    location = StringField('Location', validators=[DataRequired(), Length(max=100)])
    salary = StringField('Salary', validators=[Length(max=50)])
    category = SelectField('Category', choices=[
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('remote', 'Remote'),
        ('internship', 'Internship'),
        ('contract', 'Contract')
    ], validators=[DataRequired()])
    submit = SubmitField('Post Job')

class ApplicationForm(FlaskForm):
    cover_letter = TextAreaField('Cover Letter', validators=[DataRequired(), Length(min=50, max=1000)])
    submit = SubmitField('Submit Application')

class SearchForm(FlaskForm):
    keyword = StringField('Keywords')
    location = StringField('Location')
    category = SelectField('Category', choices=[
        ('', 'All Categories'),
        ('full-time', 'Full Time'),
        ('part-time', 'Part Time'),
        ('remote', 'Remote'),
        ('internship', 'Internship'),
        ('contract', 'Contract')
    ])
    submit = SubmitField('Search')