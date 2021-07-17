# Display Ergonomia - dht_loop

# Se obtienen lecturas del sensor DHT22 cada 2 segundos aproximadamente

# Importar módulos
import json
import time
import Adafruit_DHT

# Objetos
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
data = {} #diccionario vacío

# Lecturas ==========================================

while (True):
  time.sleep(2.0) #esperar
  # Leer DHT22 ----------------------------------------
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
  #
  # valor cero en caso de error
  #if humidity is None:
  #  humidity = 0
  #if temperature is None:
  #  temperature = 0
  #
  # Mejor enviar dato solo si no hubo error
  if humidity is not None and temperature is not None:
    # pasar a diccionario
    data["dht"] = {
      "humidity": humidity,
      "temperature": temperature
    }
    print(json.dumps(data)) #exportar datos
