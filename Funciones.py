from Adafruit_IO import Client
import time
import numpy as np

# Configuración de Adafruit IO
ADAFRUIT_IO_USERNAME = "ADAFRUIT_IO_USERNAME"
ADAFRUIT_IO_KEY = "ADAFRUIT_IO_KEY"
aio = Client(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Parámetros de la señal
num_puntos = 50 
T = 2 * np.pi  # Período de la onda

def generar_seno_coseno():
    t = np.linspace(0, 1, num_puntos) 
    x = t * T 
    y_sin = np.sin(x) / 10  # Generamos la onda de seno con amplitud reducida
    y_cos = np.cos(x) / 10  # Generamos la onda de coseno con amplitud reducida
    return y_sin.tolist(), y_cos.tolist()  # Convertimos a lista para compatibilidad

def enviar_datos(feed, datos):
    for valor in datos:
        aio.send(feed, valor)
        time.sleep(1)  # Reducimos el tiempo entre envíos para mejorar continuidad
    print(f"Datos de {feed} enviados exitosamente...")

# Generar y enviar datos
y_sin, y_cos = generar_seno_coseno()
enviar_datos("sen", y_sin)
enviar_datos("cos", y_cos)
