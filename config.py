import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'dev-secret-key'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///skillhub.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    #initialise a database URI for the application to use, and set track modifications to false to avoid overhead.