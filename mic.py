## Código para probar sensor de sonido KY-037 (micrófono)
# Tomar varias muestras y obtener el voltaje pico-pico

N = 10 #número de muestras

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
  print(':)')

#end = time.time()
#print('time ', end - start)
