# necessary modules and initialize the I2C bus
import board
import busio
i2c = busio.I2C(board.SCL, board.SDA)

# module for the board
import adafruit_ads1x15.ads1115 as ADS

# ADS1x15 library's version of AnalogIn
from adafruit_ads1x15.analog_in import AnalogIn

# create the ADC object
ads = ADS.ADS1115(i2c)

# Now let's see how to get values from the board. You can use
# these boards in either single ended or differential mode.

# single ended
# use AnalogIn to create the analog input channel, providing
# the ADC object and the pin to which the signal is attached
chan0 = AnalogIn(ads, ADS.P0)
chan1 = AnalogIn(ads, ADS.P1)
chan2 = AnalogIn(ads, ADS.P2)

# you can read using the value or voltage property
print(chan0.value, chan0.voltage)
print(chan1.value, chan1.voltage)
print(chan2.value, chan2.voltage)
