from flask import request,json
from app.models import Usuario
from app.utils.encriptacion import verify


def login():
    body = request.get_json()
    print(body)
    email = body["email"]
    password = body["password"]
    try:
        user = Usuario.query.filter(Usuario.email == email).first()
        if user == None:# or user.password!= password: #passwordescrip
            return json.dumps({"success": False, "message": "Usuario no encontrado"})
        
        if (not verify(password,user.password)):
            return json.dumps({"success": False, "message": "Contraseña incorrecta"})

        else:
            return json.dumps({"success": True})
    except:
        return json.dumps({"success": False})

