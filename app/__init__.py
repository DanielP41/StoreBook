from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object('app.config.Config')  # Asegúrate de que esto coincida con el nombre de tu clase Config

db = SQLAlchemy(app)

from app import routes, models
