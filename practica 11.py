# Blink con tiempo variable (Mapeado de señal analógica)
from machine import ADC, Pin
from utime import sleep

# Configuración de periféricos
pot = ADC(Pin(27))       # Potenciómetro conectado a GP27
led = Pin(1, Pin.OUT)    # LED externo conectado a GP1 (con resistencia)

# Función para mapear rangos (similar a la función map() de Arduino)
def mapear(valor, minimo_origen, maximo_origen, minimo_destino, maximo_destino):
    return minimo_destino + (valor - minimo_origen) * (maximo_destino - minimo_destino) / (maximo_origen - minimo_origen)

print("Control de Blink iniciado. Gira el potenciómetro...")

while True:
    # 1. Leer el valor bruto del potenciómetro (0 a 65535)
    raw = pot.read_u16()
    
    # 2. Mapear ese valor a un rango de tiempo en segundos (0.0 a 1.0 segundos)
    delay = mapear(raw, 0, 65535, 0, 1)
    
    # 3. Mostrar los datos en la consola de Thonny
    print(f"Valor ADC: {raw} | Retardo: {delay:.2f}s")
    
    # 4. Secuencia de parpadeo usando el retraso calculado
    led.value(1)   # Enciende el LED
    sleep(delay)   # Espera el tiempo del potenciómetro
    led.value(0)   # Apaga el LED led
    sleep(delay)   # Espera el tiempo del potenciómetro