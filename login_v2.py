BASE_DATOS = {
    "Andres" : "Andres1234*",
    "Juan" : "Juan1234*",
    "Sara" : "Sara1234*"
    }

intentos = 0

while intentos < 3:
    
    user = input(f"Ingrese usuario: ")
    user = user.strip().capitalize()
    
    if user in  BASE_DATOS:
        password = input(f"Ingrese contraseña: ")
        password = password.strip()
       
        if BASE_DATOS[user] == password:
            print(f"Bienvenido {user}, verifica cualquier novedad")
            break
        else:
             print("Contraseña incorrecta")
             intentos += 1
        
    else:
        print(f"User {user} no registrado")
        intentos += 1