# test program for dlp_io8_ds

from dlpio8ds import DlpIo8Ds

dlp = DlpIo8Ds()

print("\ndlp-io8-ds Test Programm\n")
for temp_nr in range(0, 5):
    print(f"Temp Sensor Nr {temp_nr}: {dlp.read_temp(temp_nr)}°C")
