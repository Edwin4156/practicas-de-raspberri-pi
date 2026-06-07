from machine import Pin
from time import sleep

# Setup Pines de Salida (GP0 a GP3)
pin_a = Pin(0, Pin.OUT) # Bit más significativo (MSB) -> b[0]
pin_b = Pin(1, Pin.OUT)
pin_c = Pin(2, Pin.OUT)
pin_d = Pin(3, Pin.OUT) # Bit menos significativo (LSB) -> b[3]

# Función contador para activar cada salida
def contador(a): 
    b = "{0:04b}".format(a) # Convierte el número a formato binario de 4 bits (ej. "0101")
    print('Binario:', b, ' | Decimal:', a) # Corregido: cambiamos 'i' por 'a'
    
    # Asigna cada bit del texto al pin correspondiente
    pin_a.value(int(b[0]))
    pin_b.value(int(b[1]))
    pin_c.value(int(b[2]))
    pin_d.value(int(b[3]))

# Bucle principal que cuenta de 0 a 15
while True: 
    for i in range(16): # El 16 es el límite, cuenta desde 0 hasta 15
        contador(i)     # Envía el número actual a la función
        sleep(1)        # Espera 1 segundo antes de pasar al siguiente número