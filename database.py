# Writing values in external database

from sqlalchemy import create_engine, text

# dotenv and environment variables reading
from dotenv import load_dotenv
import os
load_dotenv()  # take environment variables from .env.
DATABASE_URL = os.getenv('IOT_DATABASE_URL')

engine = create_engine(DATABASE_URL) # , echo=True)

def send_values2db(sensors):

    sql_insert = "INSERT INTO data(sensor_code, value) VALUES "
    for sensor in sensors:
        sql_insert += f"('{sensor[0]}', {sensor[1]}), "
    sql_insert = sql_insert[:-2] + ';'

    with engine.connect() as conn:
        conn.execute(text(sql_insert))
        conn.commit()
