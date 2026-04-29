# Se define la duración total del bucle en 60 iteraciones
duration = 60
# Se inicializa la cuenta regresiva en 30
countdown = 30

# El bucle se ejecutará 60 veces (de 0 a 59)
for second in range(duration):
    # Imprime el valor actual de la cuenta regresiva en cada ciclo
    print("Countdown:", countdown)
    
    # Solo disminuye la cuenta regresiva si es mayor a 0
    # Esto evita que el número tenga valores negativos
    if countdown > 0:
        countdown -= 1

# Al terminar todas las 60 iteraciones del bucle, imprime este mensaje
print("Session expired")