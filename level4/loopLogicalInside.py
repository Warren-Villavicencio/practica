import time

duration = 60
countdown = 30

print("Iniciando simulación...")
for second in range(duration):
    print(f"Countdown: {countdown}")
    
    if countdown > 0:
        time.sleep(1)  # Simula un segundo de tiempo real
        countdown -= 1
    else:
        # Se detiene el bucle en cuanto llega a 0, evitando repeticiones de más
        break

print("Session expired")