"""
================================================================================
EXPLICACIÓN DEL CÓDIGO ACTUAL
================================================================================
"""

# 1. Datos almacenados: Simula la información guardada en una base de datos para un usuario.
username = "EmilyVP"
password = "Safety1st!"
locked = False

# 2. Datos de entrada: Simula la información proporcionada por el usuario al intentar entrar.
attempt = "Safety1st!"
code_sent = 836027
code_entered = 836027

# 3. Lógica de autenticación:
# Evalúa tres condiciones booleanas al mismo tiempo mediante el operador 'and'.
# Todas deben ser verdaderas (True) para que el inicio de sesión sea exitoso:
#   - locked == False: Verifica que la cuenta no esté bloqueada.
#   - attempt == password: Verifica que la contraseña ingresada sea correcta.
#   - code_entered == code_sent: Verifica que el código de doble factor sea correcto.
if locked == False and attempt == password and code_entered == code_sent:
    print("✅ Login successful")
else:
    print("❌ Login failed")

"""
================================================================================
CÓMO REUTILIZAR ESTE CÓDIGO EN EL FUTURO (PRINCIPIOS SOLID)
================================================================================
Para escalar este código en proyectos reales, deberíamos reestructurarlo siguiendo 
los principios de diseño SOLID, especialmente:

1. Principio de Responsabilidad Única (SRP):
   - Problema actual: El script hace todo (define datos, simula el intento y valida).
   - Solución: Crear una clase o función (ej. `Authenticator`) cuya ÚNICA responsabilidad 
     sea validar las credenciales. Los datos del usuario deben venir de otra clase (ej. `UserRepository`).

2. Principio de Abierto/Cerrado (OCP):
   - Problema actual: Si agregamos validación por huella digital, hay que modificar este 'if'.
   - Solución: Usar un patrón de diseño donde la clase `Authenticator` reciba una lista 
     de "Reglas de Validación". Así, si hay una nueva regla, solo agregamos una clase nueva 
     sin tocar el código base del autenticador.

3. Principio de Inversión de Dependencias (DIP):
   - Problema actual: La lógica depende de variables sueltas directamente en el archivo (hardcoded).
   - Solución: El autenticador debería depender de abstracciones (interfaces) de usuarios 
     y credenciales, pasadas como parámetros o inyectadas, haciéndolo completamente reutilizable.

Ejemplo rápido de SRP y DIP:
---------------------------------------------------------
class AuthValidator:
    def is_valid(self, user, attempt):
        if user.is_locked: return False
        if user.password != attempt.password: return False
        if user.two_factor_code != attempt.two_factor_code: return False
        return True
---------------------------------------------------------
"""