
# Lectura de un valor Analógico con la Raspberry Pi Pico
from machine import ADC, Pin
import time

# Configura el pin GP26 como entrada analógica (ADC 0)
potenciometro = ADC(Pin(26)) 

print("Iniciando lectura del potenciómetro... Gira la perilla.")

while True:
    # Lee el valor analógico y lo guarda en una variable
    valor = potenciometro.read_u16()
    
    # Imprime el valor en la consola de Thonny
    print(f"Valor ADC: {valor}")
    
    # Espera 50 milisegundos antes de la siguiente lectura
    time.sleep_ms(50)