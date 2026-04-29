username = "CreativeDeflector"
password = "Love2MakeDecks!"
locked = True

new_pwd = "w0rkislif3"
confirm_pwd = "w0rkislif3"

if new_pwd == confirm_pwd:
    password = new_pwd
    print("Contraseña restablecida exitosamente")
    pwd_changed = True
else:
    print("Las contraseñas no coinciden")
    pwd_changed = False

if pwd_changed:
    print("Cuenta desbloqueada")
    locked = False
else:
    print("Intenta de nuevo")

print("Usuario:", username)
