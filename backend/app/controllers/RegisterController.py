from app import request,db
from flask import json
from app.models import Usuario

def register():
    body = request.get_json()
    user = Usuario(email=body["newEmail"],password=body["newPassword"],nombre=body["newNombre"],apellido=body["newApellido"])
    try:
        db.session.add(user)
        db.session.commit
    except:
        return json.dumps({"success":False, "nombre": user.nombre, "apellidos": user.apellido})
    return json.dumps({"success": True, "nombre": user.nombre, "email": user.email})