# necessary modules and initialize the I2C bus
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

import time

# module for the board
import adafruit_ads1x15.ads1115 as ADS
import adafruit_ads1x15

# ADS1x15 library's version of AnalogIn
from adafruit_ads1x15.analog_in import AnalogIn

# create the ADC object
ads = ADS.ADS1115(i2c)
#ads.gain = 1
#ads.data_rate = 860

#print(ads.i2c) #atributo no existe
print(ads.data_rate)
print(ads.gain)
print(ads.gains)
print(ads.mode)
print(ads.rate_config)
print(ads.rates)
print(ads.bits)
print(adafruit_ads1x15.ads1x15.Mode)

# Now let's see how to get values from the board. You can use
# these boards in either single ended or differential mode.

# single ended
# use AnalogIn to create the analog input channel, providing
# the ADC object and the pin to which the signal is attached
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)

start = time.time()
end = time.time()

# you can read using the value or voltage property
start = time.time()

print(chan0.value, chan0.voltage)
#end = time.time()
print(chan1.value, chan1.voltage)
print(chan2.value, chan2.voltage)

end = time.time()

print('time ', end - start)
