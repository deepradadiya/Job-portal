import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    SECRET_KEY = os.getenv('SECRET_KEY') or 'your-secret-key-here'
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL') or 'postgresql://localhost/jobportal'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    BOOTSTRAP_BOOTSWATCH_THEME = 'minty'