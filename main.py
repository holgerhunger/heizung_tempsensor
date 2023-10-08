# Heizung Raspberry Pi
# bei jeden Aufruf: DS18B20 Temperatur Sensoren Abfragen und in externe Datenbank schreiben
# V1.0 07.10.2023
# © 2023 Holger Hunger

# TODO: dot env zufügen
# TODO: Logging einbinden
# TODO: datenbank anbindung
# TODO: Daten abfragen und gemeinsam senden

from dlpio8ds import DlpIo8Ds
import os
from models import Data
from database import SessionLocal # , engine
from typing import Annotated
from sqlalchemy.orm import Session


username = os.environ.get("username")
password = os.environ.get("password")

dlp = DlpIo8Ds()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# db = Annotated[Session, get_db]

for temp_nr in range(0, 5):
    print(f"Temp Sensor Nr {temp_nr}: {dlp.read_temp(temp_nr)}°C")

with Annotated[Session, get_db] as db:
    print(db.query(Data).all())
