import serial
import time
import sys

class DlpIo8Ds:

    def __init__(self, port="/dev/ttyUSB0"):
        self.MESSSTELLEN_KENNUNG = ['HZHKVL',
                                    'HZHKRL',
                                    'HZWWVVM',
                                    'HZWWVNM',
                                    'HZWWRL',
                                    'NA',
                                    'NA',
                                    'NA']
        self.MESSSTELLEN_NAME = ['Heizkreis Vorlauf',
                                 'Heizkreis Rücklauf',
                                 'WW Vorlauf vor Mischer',
                                 'WW Vorlauf nach Mischer',
                                 'WW Rücklauf',
                                 'NA', 'NA', 'NA']
        self.DLP_TEMP_READ_COMMANDS = [b'9', b'0', b'=', b'-', b'[', b'O', b'P', b']']
        # self.DLP_TEMP_READ_COMMANDS = [b'9', b'0', b'-', b'=', b'O', b'P', b'[', b']']
        self.DLP_PING_COMMAND = b"'"
        self.DLP_SET_C_COMMAND = b";"
        self.port = port
        with serial.Serial(port=self.port,
                           baudrate=115200,
                           bytesize=serial.EIGHTBITS,
                           parity=serial.PARITY_NONE,
                           timeout=20000) as ser:
            #DLP Ping
            ser.write(self.DLP_PING_COMMAND)
            response = ser.read(1)
            if response != b'Q':
                print('DLP Error! No ping answer.')
                sys.exit(1)
            else:
                pass
            #DLP set to °C
            ser.write(self.DLP_SET_C_COMMAND)

    def read_temp(self, sensor_nr):
        if sensor_nr < 0 or sensor_nr > 7:
            return 888.88
        with serial.Serial(port=self.port,
                           baudrate=115200,
                           bytesize=serial.EIGHTBITS,
                           parity=serial.PARITY_NONE,
                           timeout=20000) as ser:

            for loop in range(0, 5):
                time.sleep(0.1)
                ser.write(self.DLP_TEMP_READ_COMMANDS[sensor_nr])
                response = ser.readline().decode('cp437').rstrip()
                temp_float = float(response[:-2])
                if temp_float != 999.99:
                    break

            return self.MESSSTELLEN_NAME[sensor_nr], self.MESSSTELLEN_KENNUNG[sensor_nr], temp_float
