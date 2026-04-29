import time

# Variable que define el número máximo de iteraciones permitidas en el bucle
duration = 60
# Variable que define el valor inicial de la cuenta regresiva
countdown = 30

print("Iniciando simulación...")

# Iniciamos un bucle que intentará ejecutarse 'duration' cantidad de veces
for second in range(duration):
    # Imprimimos el estado actual de la cuenta regresiva
    print(f"Countdown: {countdown}")
    
    # Comprobamos si la cuenta regresiva aún no ha llegado a cero
    if countdown > 0:
        time.sleep(1)  # Pausamos la ejecución del programa durante 1 segundo
        countdown -= 1 # Reducimos la cuenta regresiva en 1
    else:
        # Se detiene el bucle en cuanto llega a 0, evitando iteraciones innecesarias
        # aunque el 'duration' original fuese mayor (ej. iteraciones 31 a 60 se cancelan)
        break

# Este mensaje se imprime cuando el bucle ha terminado (por llegar la duración a su fin o por el 'break')
print("Session expired")