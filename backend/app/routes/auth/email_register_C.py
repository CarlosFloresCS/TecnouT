from flask import Blueprint
from app.controllers.auth.email_register_C import register

email_register_bp = Blueprint('email_register_bp',__name__)
email_register_bp.route("/register",methods=["POST"])(register)
