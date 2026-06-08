Leer un valor analógico desde un pin
Ajustando el valor leído del canal a un valor analógico que variara entre 0 y
3.3 v
#Manejando una entrada analógica
from machine import ADC, Pin
import time
adc = ADC(27) #Designamos el pin de lectura en GP27
try:
while True:
adcValue = adc.read_u16()
#Escalamos la señal
voltage = adcValue / 65535.0 * 3.3
print("ADC Valor:",adcValue, "Voltaje:", voltage, "V")
time.sleep(0.1)
except:
pass
