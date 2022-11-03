from os import abort
from flask import render_template, request, redirect, Flask, session, abort, jsonify, json
from app.models import Usuario
from app import db

def login():
    body = request.get_json()
    print(body)
    email = body["email"]
    password = body["password"]
    try:
        user = Usuario.query.filter(Usuario.email == email).first()
        if user == None or user.password!= password:
            return json.dumps({"success": False})
        else:
            return json.dumps({"success": True})
    except:
        return json.dumps({"success": False})

def register():
    body = request.get_json()
    user = Usuario(email=body["newEmail"],password=body["newPassword"],nombre=body["newNombre"],apellido=body["newApellido"])
    try:
        db.session.add(user)
        db.session.commit
    except:
        return json.dumps({"success":False, "nombre": user.nombre, "apellidos": user.apellido})
    return json.dumps({"success": True, "nombre": user.nombre, "email": user.email})