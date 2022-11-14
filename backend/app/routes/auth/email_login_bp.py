from flask import Blueprint
from app.controllers.auth.email_login_C import login

email_login_bp = Blueprint('email_login_bp',__name__)
email_login_bp.route("/login",methods=["GET","POST"])(login)
#login_bp.route("/", methods=["GET","POST"])(login)
