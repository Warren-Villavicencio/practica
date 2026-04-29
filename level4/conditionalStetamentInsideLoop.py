# 'duration' define cuánto durará la sesión completa o el bucle en iteraciones (simulando segundos).
# Reutilización: Puedes cambiar este valor para hacer la sesión global más larga o más corta.
duration = 60

# 'countdown' es el tiempo de vida o validez del código.
# Reutilización: Modifica este valor inicial cuando necesites que un código sea válido por más o menos tiempo.
countdown = 30

# Inicia un bucle que se ejecuta 'duration' veces. Cada iteración representa un segundo transcurrido en la sesión global.
# Reutilización: Este patrón for se puede reutilizar para evaluar lógicas temporales o animaciones frame a frame.
for second in range(duration):
    
    # Evalúa si el temporizador del código llegó a cero para establecer su estado actual.
    # Reutilización: Este bloque if/else sirve para definir las variables o estados principales antes de usarlos.
    if countdown == 0:
        status = "expired ❌"
    else:
        status = "active ✅"
        
    # Condición especial para el estado de advertencia, cuando quedan 10 o menos unidades de tiempo sin llegar a cero.
    # Reutilización: Útil para disparar alertas visuales a los usuarios antes de un cierre de sesión u otra acción crítica.
    if countdown > 0 and countdown <= 10:
        status = "warning ⚠️"
        
    # Imprime un mensaje diferente dependiendo de si el código ya expiró o si sigue vigente.
    # Reutilización: Sirve para dar retroalimentación dinámica si se usa en una interfaz o log de actividad.
    if status == "expired ❌":
        left = duration - second # Muestra el tiempo restante que le queda a la sesión global.
        print("Code", status, "Request new code?", left)
    else:
        print("Code", status, countdown)
        
    # Descuenta una unidad al tiempo de vida del código si este aún no llega a cero.
    # Reutilización: Es la pieza clave para cualquier tipo de cronómetro inverso, asegurando que no baje de cero.
    if countdown > 0:
        countdown -= 1

# Mensaje final al agotarse el total de iteraciones determinadas por 'duration'.
# Reutilización: Ejecutar lógicas de limpieza de variables o redirección cuando todo se agota.
print("Session expired")
