# Control de LED por Bluetooth (UART) con Raspberry Pi Pico
from machine import Pin, UART
import time

# Inicializa el módulo UART0
# Usamos GP0 como TX (Transmisión) y GP1 como RX (Recepción) a 9600 baudios (por defecto en HC-05)
uart = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# LED indicador en el pin GP13
led = Pin(13, Pin.OUT)

print("Módulo Bluetooth inicializado. Esperando comandos...")

while True:
    # Verifica si hay bytes disponibles en el buffer del UART
    if uart.any() > 0:
        # Lee todos los bytes disponibles
        raw_data = uart.read()
        
        try:
            # Convierte los bytes (b'on') a una cadena de texto común ('on')
            data = raw_data.decode('utf-8').strip().lower()
            print(f"Recibido raw: {raw_data} -> Texto: {data}")
            
            # Evaluamos el comando de texto ya limpio
            if "on" in data:
                led.value(1)
                print("LED encendido")
                uart.write("LED encendido\r\n") # Envía respuesta de vuelta al celular
                
            elif "off" in data:
                led.value(0)
                print("LED apagado")
                uart.write("LED apagado\r\n")
                
        except Exception as e:
            print(f"Error al decodificar datos: {e}")
            
    time.sleep_ms(50) # Pequeña pausa para no saturar el procesador