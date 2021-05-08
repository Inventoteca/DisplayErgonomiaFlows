# Display Ergonomia - sensors

# Se obtienen lecturas de los siguientes sensores

# - TSL2561 (lux visible)
# - ML8511 (luz UV)
# - MQ-135 (calidad del aire)
# - KY-037 (sonido)

# Los 3 últimos sensores se leen a través del ADS1115
# El sensor DHT22 (temperatura y humedad) se lee en dht_loop.py,
# se movió a otro script para muestrear lo más rápido posible en este script.

# funcion para calcular relacion lineal
def mapf(x, in_min, in_max, out_min, out_max):
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Importar módulos
import json
import time
import board
import busio
import adafruit_tsl2561
import adafruit_ads1x15.ads1115 as ADS
from adafruit_ads1x15.analog_in import AnalogIn

# Contantes
UV_INDEX_MULT = 2.1 #multiplicador para obtener índice UV
MQ_OFFSET = 0.090 #voltaje de salida con aire limpio
MQ_MULT = 1000.0 #multiplicador para convertir a ppm
MQ_N = 10 #número de muestras sensor MQ-135
MQ_T = 0.0 #tiempo entre lecturas sensor MQ-135
KY_MULT = 800.0 #multiplicador para decibeles
KY_N = 100 #número de muestras
KY_T = 0.0 #tiempo de espera entre muestras

# Objetos
i2c = busio.I2C(board.SCL, board.SDA)
ads = ADS.ADS1115(i2c)
tsl = adafruit_tsl2561.TSL2561(i2c)
tsl.gain = 0 #0=1x, 1=16x
tsl.integration_time = 0 #0=13.7ms, 1=101ms, 2=402ms, or 3=manual
data = {} #diccionario vacío

# Canales del ADC
chan0 = AnalogIn(ads, ADS.P0) #ML8511 (luz uv)
chan1 = AnalogIn(ads, ADS.P1) #MQ-135 (aire)
chan2 = AnalogIn(ads, ADS.P2) #KY-037 (sonido)

# Lecturas ==========================================

while (True):
  #Leer TSL2561 (lux) -------------------------------
  broadband = tsl.broadband
  infrared = tsl.infrared
  lux = tsl.lux
  if lux is None:
    lux = 0
  #pasar a diccionario
  data["light"] = {
    "broadband": broadband,
    "infrared": infrared,
    "lux": lux
  }
  
  # Leer ML8511 (luz UV) ----------------------------
  uv_voltage = chan0.voltage
  uv_intensity = mapf(uv_voltage, 0.985, 2.2, 0.0, 10.0)
  uv_index = uv_intensity * UV_INDEX_MULT
  # pasar a diccionario
  data["uv"] = {
    "voltage": uv_voltage,
    "intensity": uv_intensity,
    "index": uv_index
  }
  
  # Leer MQ-135 (calidad del aire) -------------------
  val = chan1.voltage #primera lectura
  sum_ = val #sumatoria
  
  for _ in range(MQ_N - 1):
    val = chan1.voltage #nueva lectura
    sum_ += val #agregar a la suma
    time.sleep(MQ_T) #esperar un poco
  
  avg = sum_ / MQ_N #promedio
  ppm = (avg - MQ_OFFSET) * MQ_MULT #particulas por millón
  # pasar a diccionario
  data["gas"] = {
    "voltage": avg,
    "ppm": ppm
  }
  
  # Leer KY-037 (sonido) --------------------------
  val = chan2.voltage #primera lectura
  min_ = val
  max_ = val
  sum_ = val
  
  for _ in range(KY_N - 1):
    val = chan2.voltage #nueva lectura
    min_ = min(min_, val) #guardar el minimo
    max_ = max(max_, val) #guardar el maximo
    sum_ += val #agregar a la suma
    time.sleep(KY_T) #esperar un poco
  
  avg = sum_ / KY_N #promedio
  dif = max_ - min_ #diferencia (V pico-pico)
  dB = dif * KY_MULT #decibeles
  #pasar a diccionario
  data["sound"] = {
    "avg": avg,
    "max": max_,
    "min": min_,
    "dif": dif,
    "dB": dB
  }
  
  print(json.dumps(data)) #exportar datos
  time.sleep(0.1) #esperar antes del siguiente loop
