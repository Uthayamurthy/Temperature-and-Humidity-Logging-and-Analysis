import Adafruit_DHT
from time import sleep, strftime
import csv

DHT_SENSOR = Adafruit_DHT.DHT22
DHT_PIN = 4

with open('data.csv', 'w') as csv_file:
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow('date,time,temperature,humidity')
    while True:
        humidity, temperature = Adafruit_DHT.read_retry(DHT_SENSOR, DHT_PIN)
        if humidity is not None and temperature is not None:
            temp = str(round(temperature, 2))
            hum = str(round(humidity, 2))
            date_now = strftime("%d-%m-%Y")
            time_now = strftime("%H:%M:%S")
            print(f' Temperature:{temp}*C | Humidity : {hum}% ')
            log_data = [date_now, time_now, temp, hum]
            csv_writer.writerow(log_data)
        else:
            print("Failed to retrieve data from humidity sensor")
        
        sleep(60)