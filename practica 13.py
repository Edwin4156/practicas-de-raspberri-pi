# Experimentación con un Joystick en la Raspberry Pi Pico
from machine import ADC, Pin
import time

# Función de mapeado (tipo Arduino)
def mapear(valor, minimo_origen, maximo_origen, minimo_destino, maximo_destino):
    return minimo_destino + (valor - minimo_origen) * (maximo_destino - minimo_destino) / (maximo_origen - minimo_origen)

# Definimos los canales de lectura analógica
xValue = ADC(Pin(26)) # Conectado a VRX del joystick
yValue = ADC(Pin(27)) # Conectado a VRY del joystick

# El botón (SW) es una ENTRADA. Usamos PULL_UP porque el joystick suele mandar un 0 (GND) al presionarse.
boton = Pin(1, Pin.IN, Pin.PULL_UP)

print("Joystick inicializado. Mueve la palanca o presiona el botón...")

while True:
    # 1. Leer los valores brutos de los ejes (0 a 65535)
    raw_x = xValue.read_u16()
    raw_y = yValue.read_u16()
    
    # 2. Mapear los valores a un rango de 0.0 a 10.0
    x_mapeado = mapear(raw_x, 0, 65535, 0, 10)
    y_mapeado = mapear(raw_y, 0, 65535, 0, 10)
    
    # 3. Leer el estado físico del botón electrónico
    # Debido al PULL_UP: 1 significa SIN presionar, 0 significa PRESIONADO
    estado_boton = boton.value()
    
    # 4. Cambiar el texto del botón para que sea fácil de leer en consola
    texto_boton = "PRESIONADO" if estado_boton == 0 else "SUELTO"
    
    # 5. Imprimir los resultados con dos decimales en la consola de Thonny
    print(f"X: {x_mapeado:.2f} | Y: {y_mapeado:.2f} | Botón: {texto_boton}")
    
    # Pequeña pausa para no saturar la consola
    time.sleep(0.1)