import os

class Config:
    SQLALCHEMY_DATABASE_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:12345@localhost/data_leak_prevention')
    SQLALCHEMY_TRACK_MODIFICATIONS = False