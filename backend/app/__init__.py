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
from app.routes.auth.email_login_bp import email_login_bp
from app.routes.auth.email_register_C import email_register_bp

app.register_blueprint(email_login_bp, url_prefix="/auth")
app.register_blueprint(email_register_bp, url_prefix="/auth")
db.create_all()