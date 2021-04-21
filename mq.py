## Probar sensor MQ-135
# Semiconductor Sensor for Air Quality Control. MQ135 gas sensor has high
# sensitity to Ammonia, Sulfide and Benze steam, also sensitive to smoke and
# other harmful gases. It is with low cost and suitable for different applications.


# funcion para calcular relacion lineal
def mapf(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Constantes
OFFSET = 0.090 #voltaje de salida con aire limpio
FACTOR = 1000.0 #factor para convertir a ppm
N = 10 #número de muestras
T = 0.1 #tiempo entre lecturas

# necessary modules and initialize the I2C bus
import time
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

# module for the board
import adafruit_ads1x15.ads1115 as ADS

# ADS1x15 library's version of AnalogIn
from adafruit_ads1x15.analog_in import AnalogIn

# create the ADC object
ads = ADS.ADS1115(i2c)

# Now let's get values from the board. You can use
# these boards in either single ended or differential mode.

# single ended
# use AnalogIn to create the analog input channel, providing
# the ADC object and the pin to which the signal is attached
chan1 = AnalogIn(ads, ADS.P1)

# you can read using the value or voltage property
# Se pueden tomar varias muestras para mejor lectura
val = chan1.voltage # primera lectura
#min_ = val
#max_ = val
sum_ = val

for _ in range(N-1):
  #print(i)
  val = chan1.voltage #nueva lectura
  #min_ = min(min_, val) #guardar el minimo
  #max_ = max(max_, val) #guardar el maximo
  sum_ += val #agregar a la suma
  time.sleep(T) #esperar un poco

avg = sum_ / N #promedio

ppm = (avg - OFFSET) * FACTOR #particulas por millón
print('{"v":', avg, ',"ppm":',ppm, '}')
