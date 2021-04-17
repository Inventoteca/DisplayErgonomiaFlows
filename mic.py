## Código para probar sensor de sonido KY-037 (micrófono)
# Tomar varias muestras y obtener el voltaje pico-pico

N = 30 #número de muestras
T = 0.1 #tiempo de espera entre muestras

# necessary modules and initialize the I2C bus
import board
import busio
import time
i2c = busio.I2C(board.SCL, board.SDA)

# module for the ADC
import adafruit_ads1x15.ads1115 as ADS

# ADS1x15 library's version of AnalogIn
from adafruit_ads1x15.analog_in import AnalogIn

# create the ADC object
ads = ADS.ADS1115(i2c)

# Now get values from the board in single ended mode.
# use AnalogIn to create the analog input channel, providing
# the ADC object and the pin to which the signal is attached
chan2 = AnalogIn(ads, ADS.P2)

# variables to measure elapsed time
#start = time.time()
#end = time.time()

# you can read using the value or voltage property
#start = time.time()

#primera lectura
val = chan2.voltage
min_ = val
max_ = val
sum_ = val

for _ in range(N):
  #print(chan2.voltage)
  val = chan2.voltage #nueva lectura
  min_ = min(min_, val) #guardar el minimo
  max_ = max(max_, val) #guardar el maximo
  sum_ += val #agregar a la suma
  time.sleep(T) #esperar un poco

avg = sum_ / N #promedio
dif = max_ - min_ #diferencia (V pico-pico)

print('Min ', min_)
print('Max ', max_)
print('Sum ', sum_)
print('Avg ', avg)
print('Dif ', dif)

#end = time.time()
#print('time ', end - start)
