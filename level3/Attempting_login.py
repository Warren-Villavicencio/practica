# Definición de credenciales del usuario (variables de prueba)
username = "ExecuTroll_404"
password = "cl1mbthel4dder"

# Contador simulado de intentos de inicio de sesión fallidos
failed_logins = 5

# Muestra de la interfaz por consola
print("""
|**************|
|  Intentando  | 
|    login...  |
|**************|
""")

# Verificación del estado de bloqueo de cuenta
# Si los intentos fallidos son menores al límite (5), permite ingresar
if failed_logins < 5:
    print("Ingrese la contraseña")

# Si se iguala o supera el límite, bloquea la cuenta y entra al flujo de recuperación
else:
    print("🔒 Cuenta bloqueada")
    
    # Inicia el flujo de recuperación de contraseña debido al bloqueo
    print("Enviando código de restablecimiento ✉️")
    
    # Validación de seguridad simulada antes de enviar el código.
    # Nota técnica: en un sistema real de restablecimiento, 
    # normalmente solo se solicitaría/verificaría el correo o el ID del usuario, y no la contraseña.
    if username == "ExecuTroll_404" and password == "cl1mbthel4dder":
        print("Correo electrónico de restablecimiento de contraseña enviado ✅")
    else:
        print("Usuario no encontrado ❌")

# Fin del script del flujo de inicio de sesión
print("Intento de inicio de sesión finalizado") 