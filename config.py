import os
SECRET_KEY = os.urandom(32)
# Grabs the folder where the script runs.
basedir = os.path.abspath(os.path.dirname(__file__))

# Enable debug mode.
DEBUG = True

# Connect to the database
database_host = os.getenv("database_host")
database_name = os.getenv("database_name")
database_user = os.getenv("database_user")
database_password = os.getenv("database_password")
if database_password:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{database_user}:{database_password}@{database_host}/{database_name}'
else:
    SQLALCHEMY_DATABASE_URI = f'postgresql://{database_user}@{database_host}/{database_name}'
SQLALCHEMY_TRACK_MODIFICATIONS = False