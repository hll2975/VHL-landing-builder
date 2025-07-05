import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY', 'clave-dev')
    SQLALCHEMY_DATABASE_URI = 'sqlite:///landing.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
