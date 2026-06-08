# Control de intensidad de un LED mediante PWM y Potenciómetro
from machine import ADC, Pin, PWM
import time

# Configuración de la entrada analógica (Potenciómetro en GP27)
adc = ADC(Pin(27))

# Configuración de la salida PWM (LED en GP7)
pwm = PWM(Pin(7))
pwm.freq(1000) # Frecuencia de 1kHz (ideal para LEDs, no parpadea a la vista humana)

print("Control PWM iniciado. Gira el potenciómetro para cambiar el brillo.")

try:
    while True:
        # Lee el valor del potenciómetro (0 a 65535)
        adcValue = adc.read_u16()
        
        # Asigna ese mismo valor al ciclo de trabajo del PWM (0 a 65535)
        pwm.duty_u16(adcValue)
        
        # Pequeña pausa para estabilizar la lectura
        time.sleep(0.1) 
        
except KeyboardInterrupt:
    # Si detienes el programa en Thonny (Ctrl+C), se limpia el pin PWM
    print("\nPrograma detenido. Apagando PWM...")
    pwm.deinit()
except Exception as e:
    # Si ocurre cualquier otro error, también asegura apagar el PWM
    print(f"Ocurrió un error: {e}")
    pwm.deinit()