# Telemetría por Bluetooth: Transmisión de Voltaje de Potenciómetro
from machine import ADC, Pin, UART
from utime import sleep

# Configuración del puerto UART0 (GP0 como TX, GP1 como RX) a 9600 baudios
serial = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Declaración del pin de lectura analógica (GP26 / ADC0)
val_pot = ADC(Pin(26))

# Factor para convertir el valor de 16 bits (0-65535) a Voltios (0-3.3V)
factor_16 = 3.3 / 65535

def main():
    print("Inicio del programa de telemetría... Transmitiendo datos.")
    
    while True:
        # 1. Leer el valor bruto del ADC y convertirlo a voltaje
        lectura_bruta = val_pot.read_u16()
        voltaje = lectura_bruta * factor_16
        
        # 2. Estructurar el mensaje con f-string limitando a 2 decimales
        # Usamos \r\n (retorno de carro y salto de línea) ideal para terminales Bluetooth
        buffer = f"Voltaje: {voltaje:.2f} V\r\n"
        
        # 3. Imprimir en la consola local de Thonny (para monitoreo)
        print(f"Enviando local: {buffer.strip()}")
        
        # 4. Enviar los datos de forma inalámbrica a través del módulo Bluetooth
        serial.write(buffer)
        
        # Esperar 2 segundos antes de la próxima transmisión
        sleep(2)

# Punto de entrada estándar de Python
if __name__ == '__main__':
    main()