# 
# Lectura de valores de temperatura y humedad desde sensor DHT-11
# y muestra de valores en pantalla OLED SSD1306 128x64
# Envio de valores cada xx segundos a traves de MQTT

import dht
import machine

# Lectura en pin 4 (D2)
d = dht.DHT11(machine.Pin(4))

# d.measure()
# d.temperature()
# d.humidity()