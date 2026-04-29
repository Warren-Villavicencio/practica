username = "warren"
password = "uitop"
score = 100
strength = 10.5
score += 10
strength += 10
score *= 2
strength *= 2
attempts = "uitop"
fails_login = 0
fails_login += 1
fails_login += 2

if fails_login >= 5:
    print("Demasiados intentos fallidos",fails_login)
else:
    print("bloqueado")

if score >= 100:
    print("Puntaje alto")
else:
    print("Puntaje bajo")

if strength >= 10.5:
    print("Fuerza alta")
else:
    print("Fuerza baja")

if attempts == password:
    print("Contraseña correcta")
else:
    print("Contraseña incorrecta")
    fails_login += 1

if username == "warren":
    print("Usuario correcto")
else:
    print("Usuario incorrecto") 
    fails_login += 1


print(username, "\n"
,"password", password, "\n"
,"score", score, "\n"
,"strength", strength, "\n"
,"password_ok", attempts==password, "\n"
,"fails_login", fails_login>=5, "\n"
)

