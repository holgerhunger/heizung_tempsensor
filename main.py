# Heizung Raspberry Pi
# bei jeden Aufruf: DS18B20 Temperatur Sensoren Abfragen und in externe Datenbank schreiben
# V0.9 07.10.2023
# V1.0 08.10.2023
# © 2023 Holger Hunger

# TODO: Logging einbinden

from database import send_values2db
from dlpio8ds import DlpIo8Ds

dlp = DlpIo8Ds()

temp_values = []

for sensor_nr in range(0, 5):
    beschreibung, sensor_id, temp = dlp.read_temp(sensor_nr)
    temp_values.append((sensor_id, temp))

send_values2db(temp_values)
