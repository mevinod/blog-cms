# config.py

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:postgres@postgres/postgres'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'your_secret_key_here'

