# Generación de tonos con un Buzzer Pasivo usando PWM
from machine import Pin, PWM
from utime import sleep

# Configuración del pin del Buzzer (GP18)
buzzer = PWM(Pin(18))

# Función para emitir un tono personalizado
def emitir_tono(frecuencia, duracion_segundos):
    buzzer.freq(frecuencia)       # Ajusta la frecuencia (Hz)
    buzzer.duty_u16(32768)        # Activa el sonido al 50% del ciclo de trabajo
    sleep(duracion_segundos)      # Mantiene el tono por el tiempo indicado
    buzzer.duty_u16(0)            # Silencia el buzzer

print("Reproduciendo secuencia de tonos de prueba...")

# Ejemplo 1: Tu tono original de 500 Hz por 1 segundo
emitir_tono(500, 1.0)

sleep(0.5) # Pausa de medio segundo en silencio

# Ejemplo 2: Una pequeña secuencia de dos tonos rápidos (tipo alerta)
emitir_tono(800, 0.1)
sleep(0.05)
emitir_tono(1200, 0.2)

# Liberar el pin al terminar el script principal
buzzer.deinit()
print("Prueba finalizada.")