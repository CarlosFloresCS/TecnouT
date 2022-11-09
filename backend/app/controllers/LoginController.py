from flask import request,json
from app.models import Usuario

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

