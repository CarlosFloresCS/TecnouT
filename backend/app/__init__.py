import os
import pathlib
from flask import Flask
from config import Config
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#app.secret_key = "proyectoDBP"
cors = CORS(app)
app.config.from_object(Config)
db = SQLAlchemy(app)


from app import models, topRoutes
from app.routes.login_bp import *
from app.routes.register_bp import *

app.register_blueprint(login_bp, url_prefix="/login")
app.register_blueprint(register_bp, url_prefix="/register")
db.create_all()