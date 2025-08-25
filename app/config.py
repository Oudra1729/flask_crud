import os

class Config:
    SQLALCHEMY_DATABASE_URI = "postgresql://postgres:root@localhost:5432/flaskdb"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
