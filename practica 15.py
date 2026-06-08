# Alarma optimizada con Tabla de Búsqueda (LUT)
from machine import Pin, PWM
import math
import time

boton = Pin(20, Pin.IN, Pin.PULL_UP)
buzzer = PWM(Pin(18))

# --- GENERACIÓN DE LA LOOK-UP TABLE (Se ejecuta solo una vez al arrancar) ---
frecuencias_sirena = []
for x in range(0, 36):
    radianes = (x * 10) * math.pi / 180
    toneVal = 1500 + int(math.sin(radianes) * 500)
    frecuencias_sirena.append(toneVal)
# ----------------------------------------------------------------------------

def alert(): 
    # Recorre la lista de frecuencias precalculadas
    for frecuencia in frecuencias_sirena:
        buzzer.freq(frecuencia)
        time.sleep_ms(10)

print("Sistema optimizado listo. Presiona GP20...")

try:
    while True:
        if not boton.value():
            buzzer.duty_u16(8000)
            alert()
        else:
            buzzer.duty_u16(0)
            time.sleep_ms(50)

except KeyboardInterrupt:
    print("\nPrograma interrumpido.")
    buzzer.deinit()