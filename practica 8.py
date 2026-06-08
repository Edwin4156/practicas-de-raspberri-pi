import dht
import machine
import time

# Configuración del pin (Pin 4 de la Raspberry Pi Pico)
sensor = dht.DHT11(machine.Pin(4))

print("Iniciando lectura del sensor DHT11... (Espera 2 segundos)")
time.sleep(2)

while True:
    try:
        # El DHT11 necesita un pequeño respiro entre lecturas
        time.sleep(2)
        
        # Realiza la medición
        sensor.measure()
        
        # Almacena los datos en las variables
        temp = sensor.temperature()
        hum = sensor.humidity()
        
        # Muestra los resultados en la consola
        print(f"Temperatura: {temp}°C | Humedad: {hum}%")
        
    except OSError as e:
        # Si el sensor falla en una lectura, muestra el error pero NO detiene el programa
        print("Error al leer el sensor. Reintentando...")