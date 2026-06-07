from machine import Pin
import utime

# Configurar los pines GP0 a GP7 como salidas usando una lista
pines = []
for i in range(8):
    pines.append(Pin(i, Pin.OUT))

# Ejecución secuencial
while True:
    for pin in pines:
        pin.value(1)       # Pone en ON el LED actual
        utime.sleep(0.2)   # Espera 200 ms
        pin.value(0)       # Pone en OFF el LED actual
        utime.sleep(0.2)   # Espera 200 ms antes de pasar al siguiente-