import imp
from app import app,db
from app.models import *
from flask import render_template,request,json
from datetime import datetime
from flask_cors import cross_origin

@app.route("/usersjson")
@cross_origin()
def getUsers():
    users = Usuario.query.all()
    print(users)
    userList = []
    for user in users:
        userList.append({"nombre": user.nombre, "apellido": user.apellido})
    return json.dumps(userList)

@app.route('/')
def index():
    return "Inicio"