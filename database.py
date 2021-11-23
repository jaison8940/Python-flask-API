from flask_sqlalchemy import SQLAlchemy
import secret
from flaskapp import app
import psycopg2

# app.config['SQLALCHEMY_DATABASE_URI'] = f"postgresql://{secret.username}:{secret.password}@{secret.hostname}/{secret.dbname}"
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///c:\\sqlite\\test.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

