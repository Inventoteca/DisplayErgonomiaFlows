# Dependencias Display Ergonomia

# Base
sudo apt-get update
sudo apt-get upgrade

# DHT
sudo apt-get install python3-dev python3-pip
sudo python3 -m pip install --upgrade pip setuptools wheel
sudo pip3 install Adafruit_DHT

# ADS1115 y TSL2561
pip3 install Adafruit-Blinka
sudo pip3 install adafruit-circuitpython-ads1x15
sudo pip3 install adafruit-circuitpython-tsl2561

# Neopixel
curl -sS get.pimoroni.com/unicornhat | bash
#Al terminar instalar nodo para Neopixel desde pallette manager en Node-RED
#npm install node-red-node-pi-neopixel

