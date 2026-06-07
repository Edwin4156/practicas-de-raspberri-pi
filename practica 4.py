from machine import Pin
import time

# Configurar botones en GP20 y GP21 con resistencia PULL_UP interna
# (Leen 1 en reposo y 0 al ser presionados, tal como está en tus "if")
buttonA = Pin(20, Pin.IN, Pin.PULL_UP) # Inicia la cuenta
buttonB = Pin(21, Pin.IN, Pin.PULL_UP) # Detiene el contador

# Inicializamos las variables de tiempo
start_time = 0
end_time = 0
cronometro_activo = False

print("Cronómetro listo. Presiona Botón A (GP20) para iniciar...")

while True:
    # 1. DETECTAR BOTÓN A (INICIO)
    if buttonA.value() == 0: 
        start_time = time.ticks_ms() # Guarda el tiempo actual en milisegundos
        cronometro_activo = True
        print('¡Cronómetro iniciado! Esperando Botón B...')
        time.sleep_ms(300) # Antirebote (Debounce)
        
    # 2. DETECTAR BOTÓN B (FIN)
    if buttonB.value() == 0:
        if cronometro_activo:
            end_time = time.ticks_ms() # Guarda el tiempo final
            
            # Calcular la diferencia exacta usando funciones nativas de MicroPython
            tiempo_transcurrido_ms = time.ticks_diff(end_time, start_time)
            tiempo_segundos = tiempo_transcurrido_ms / 1000.0 # Convertir a segundos
            
            print("Tiempo transcurrido:", tiempo_segundos, "seg.")
            cronometro_activo = False # Resetea el estado
        else:
            print("Primero debes iniciar el cronómetro con el Botón A.")
            
        time.sleep_ms(300) # Antirebote (Debounce)
        
    time.sleep_ms(10) # Pequeña pausa para no saturar el procesador