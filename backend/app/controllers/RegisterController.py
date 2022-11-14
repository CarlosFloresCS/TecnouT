from app import db
from flask import json,request
from app.models import Usuario
from app.utils.encriptacion import sign

def register():
    print("register")
    body = request.get_json()
    print(body)
    newEmail = body["newEmail"]
    newPassword = body["newPassword"]
    newNombre = body["newNombre"]
    newApellido = body["newApellido"]
    
    if newEmail == None or newPassword == None or newNombre == None or newApellido == None:
        return json.dumps({"success": False, "message": "Vacio en los parámetros de email, password, nombre o apellido."})
    
    lenPassword = len(newPassword) # Tamaño mínimo 8 (5 letras y 3 números)
    haslenNumber = 0 # Debe tener mínimo 3 números
    haslenLetter = 0 # Debe tener mínimo 5 letras

    for letter in newPassword:
        if letter.isdigit():
            haslenNumber += 1
        if letter.isalpha():
            haslenLetter += 1
    
    if (lenPassword < 8) or (haslenNumber < 3) or (haslenLetter < 5):
        print(str(lenPassword) + " " + str(haslenNumber) + " " + str(haslenLetter))
        return json.dumps({"success": False, "message": "Contraseña invalido, requiere mínimo 3 números y 5 letras"})
    
    PasswordEncriptado = sign(newPassword)

    try:
        user = Usuario(email=newEmail,password=PasswordEncriptado,nombre=newNombre,apellido=newApellido)
        db.session.add(user)
        db.session.commit()
    except Exception as error:
        print(error)
        return json.dumps({"success":False})
    return json.dumps({"success": True})