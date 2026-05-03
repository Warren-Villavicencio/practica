"""
Explicación del código actual:
- username: Variable que almacena el nombre del usuario.
- face_id_ok: Variable booleana que simula si el reconocimiento facial fue exitoso.
- touch_id_ok: Variable booleana que simula si el reconocimiento de huella fue exitoso.
- if face_id_ok or touch_id_ok: Utiliza el operador lógico 'or' para verificar si al menos una de las dos condiciones es verdadera.
- print(...): Muestra un mensaje de éxito si alguna de las verificaciones biométricas es correcta, o un mensaje de error si ambas fallan.


Aplicación de los principios SOLID a este código (Refactorización sugerida):

1. Single Responsibility Principle (SRP - Responsabilidad Única):
   Actualmente el código define los datos, evalúa las reglas y muestra el resultado en un mismo bloque.
   Se debería separar: una clase/función para los datos del usuario, otra encargada de la validación, y otra para la presentación o respuesta.

2. Open/Closed Principle (OCP - Abierto/Cerrado):
   Si queremos agregar otra validación (ej. PIN o Retina), tendríamos que modificar el 'if'.
   Podríamos cumplir OCP usando una lista de validadores e iterando sobre ellos. Así, agregar uno nuevo no altera la lógica principal.

3. Liskov Substitution Principle (LSP - Sustitución de Liskov):
   Si creamos una interfaz genérica `BiometricMethod` con un método `is_valid()`, cualquier subclase (`FaceID`, `TouchID`) debe poder usarse de manera intercambiable sin romper el sistema.

4. Interface Segregation Principle (ISP - Segregación de Interfaces):
   Las abstracciones de validación no deberían forzar la implementación de métodos innecesarios (ej. no obligar a un validador de PIN a implementar métodos de escaneo biométrico).

5. Dependency Inversion Principle (DIP - Inversión de Dependencias):
   La lógica principal de autenticación no debe depender de variables booleanas concretas como `face_id_ok`, sino de una abstracción de alto nivel (como un servicio o interfaz de validación).
"""

username = "Micr0-Mngr" # Define el nombre de usuario a validar
face_id_ok = True       # Estado de validación por reconocimiento facial
touch_id_ok = False     # Estado de validación por huella dactilar

# Evalúa si al menos uno de los métodos biométricos fue validado exitosamente
if face_id_ok or touch_id_ok:
    print("Biometric ID verified ✅") # Se ejecuta si al menos una condición es True
else:
    print("Biometric ID not verified ❌") # Se ejecuta solo si TODAS las condiciones son False