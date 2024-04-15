import time
import pyfirmata
import requests
from dotenv import load_dotenv
import os
from logger import log_handler
import uuid

load_dotenv()

"""
board = pyfirmata.Arduino(os.getenv('PORT'))

it = pyfirmata.util.Iterator(board)
it.start()
"""

# Obtenemos la hora en el salvador, san salvador
def get_time():
    try:
        url = "https://worldtimeapi.org/api/timezone/America/El_Salvador"
        response = requests.get(url)
        data = response.json()
        hora = data['datetime'].split('T')[1].split('.')[0]
        log_handler.info(f"La hora es {hora}")
        return hora
    except Exception as e:
        log_handler.exception(f"Error al obtener la hora: {e}")

# Obtenemos la temperatura en san salvador
def get_temperature():
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key={os.getenv('API_KEY')}&q=San%20Salvador"
        response = requests.get(url)
        data = response.json()
        temperatura = data['current']['temp_c']
        log_handler.info(f"La temperatura es de {temperatura}")
        return temperatura
    except Exception as e:
        log_handler.exception(f"Error al obtener la temperatura: {e}")

# Obtenemos la humedad en san salvador
def get_humidity():
    try:
        url = f"https://api.weatherapi.com/v1/current.json?key={os.getenv('API_KEY')}&q=San%20Salvador"
        response = requests.get(url)
        data = response.json()
        humedad = data['current']['humidity']
        log_handler.info(f"La humedad es de {humedad}")
        return humedad
    except Exception as e:
        log_handler.exception(f"Error al obtener la humedad: {e}")

def main():
    hora = get_time()
    temperatura = get_temperature()
    humedad = get_humidity()

    if int(hora.split(':')[0]) >= 6 and int(hora.split(':')[0]) <= 18 and int(humedad) < 50 and int(temperatura) > 25:
        log_handler.info("Regando plantas")
        #board.digital[13].write(1)
        time.sleep(5)
        #board.digital[13].write(0)
        log_handler.info("Plantas regadas")
    else:
        log_handler.info("No se riegan las plantas")

if __name__ == '__main__':
    main()