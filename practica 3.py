from machine import Pin
import time

# Configuramos el botón en GP5 como entrada con resistencia PULL_DOWN interna
# (Esto asegura que lea 0 en reposo y 1 al presionar el botón)
button = Pin(5, Pin.IN, Pin.PULL_DOWN) 

# Configuramos el LED en GP3 como salida
led = Pin(3, Pin.OUT) 
led.value(0) # Empezamos con el LED apagado

print("Sistema Monoestable Listo. Presiona el botón...")

while True:
    if button.value() == 1:       # Si el botón se presiona (recibe 3.3V)
        led.value(1)              # Se activa el LED
        print('LED Activado')
        
        time.sleep_ms(2000)       # Mantiene el estado por 2000 ms (2 segundos)
        
        led.value(0)              # Se apaga el LED al terminar el tiempo
        print('LED Desactivado')
        print('Tiempo transcurrido: 2000 ms')
        
    else:
        led.value(0)              # Mientras no se presione, asegura que esté apagado
    
    time.sleep_ms(50)             # Una pequeña pausa para estabilidad del bucle