from machine import Pin, I2C
from micropython_i2c_lcd import I2cLcd # <-- Volvemos a 'pico_i2c_lcd'
import time

# Configuración del bus I2C (Usaremos I2C0 en los pines GP0 y GP1)
i2c = I2C(0, sda=Pin(0), scl=Pin(1), freq=400000)

# Dirección I2C típica para pantallas LCD (suele ser 0x27 o 0x3F)
I2C_ADDR = 0x27

# Inicializamos el objeto LCD (Dirección, Filas, Columnas)
lcd = I2cLcd(i2c, I2C_ADDR, 2, 16)

# Limpiar la pantalla por seguridad
lcd.clear()

# Escribir el "Hola Mundo"
lcd.move_to(0, 0) 
lcd.putstr("Hola Mundo!")

lcd.move_to(0, 1) 
lcd.putstr("Pico + I2C LCD")

while True:
    time.sleep(1)