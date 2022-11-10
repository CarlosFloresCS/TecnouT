from app import db
from flask import json,request
from app.models import Usuario

def register():
    print("register")
    body = request.get_json()
    print(body)
    user = Usuario(email=body["newEmail"],password=body["newPassword"],nombre=body["newNombre"],apellido=body["newApellido"])
    try:
        db.session.add(user)
        db.session.commit()
    except:
        return json.dumps({"success":False, "nombre": user.nombre, "apellidos": user.apellido})
    return json.dumps({"success": True, "nombre": user.nombre, "email": user.email})