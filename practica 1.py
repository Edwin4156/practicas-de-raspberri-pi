from machine import Pin
import time

# creamos el objeto LED en el pin 1 como salida
led = Pin(1, Pin.OUT)

while True:
    led.value(1)     # Pone LED en on (Indentado)
    time.sleep(0.5)  # Espera 0.5s (Indentado)
    led.value(0)     # Pone el LED en off (Indentado)
    time.sleep(0.5)  # Espera 0.5s (Indentado)	