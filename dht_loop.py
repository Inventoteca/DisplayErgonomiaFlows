# Display Ergonomia - dht_loop

# Se obtienen lecturas del sensor DHT22 cada 2 segundos aproximadamente

# Importar módulos
import Adafruit_DHT

# Objetos
DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4
data = {} #diccionario vacío

# Lecturas ==========================================

while (True):
  # Leer DHT22 ----------------------------------------
  humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
  # valor cero en caso de error
  if humidity is None:
    humidity = 0
  if temperature is None:
    temperature = 0
  # pasar a diccionario
  data["dht"] = {
    "humidity": humidity,
    "temperature": temperature
  }

  print(json.dumps(data)) #exportar datos
  time.sleep(2.0) #esperar antes del siguiente loop
