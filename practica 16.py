# Medición de distancia con sensor ultrasónico HC-SR04 y Raspberry Pi Pico
import machine
import time

# Configuración de pines
# TRIGGER es una salida (envía el pulso)
pintrig = machine.Pin(16, machine.Pin.OUT)
# ECHO es una entrada (recibe el pulso de retorno protegido por el divisor de voltaje)
pinecho = machine.Pin(15, machine.Pin.IN)

def read_ultrasonic():
    # Asegurar que el trigger empiece en bajo
    pintrig(0)
    time.sleep_us(5)
    
    # Enviar un pulso de disparo de 10 microsegundos
    pintrig(1)
    time.sleep_us(10)
    pintrig(0)
    
    # 1. Esperar a que el pin Echo pase de 0 a 1 (Inicio del viaje del sonido)
    while pinecho() == 0:
        pass
    toff = time.ticks_us() # Guarda el tiempo exacto de salida
    
    # 2. Esperar a que el pin Echo regrese de 1 a 0 (Retorno del sonido)
    while pinecho() == 1:
        pass
    ton = time.ticks_us()  # Guarda el tiempo exacto de llegada
    
    # Calcular la duración total del viaje en microsegundos
    elapsedtime = time.ticks_diff(ton, toff)
    
    # Calcular la distancia en centímetros
    # La constante 58 viene de: (Velocidad del sonido 343 m/s) invertida y dividida entre 2 (ida y vuelta)
    dist = elapsedtime / 58
    
    return dist

print("Sensor HC-SR04 iniciado. Midiendo distancia...")

while True:
    # Llamamos a la función y guardamos el resultado
    distance = read_ultrasonic()
    
    # Imprimimos la distancia con un decimal para mejor lectura
    print(f"Distancia medida: {distance:.1f} cm")
    
    # Pausa de 1 segundo antes de la siguiente lectura
    time.sleep(1)