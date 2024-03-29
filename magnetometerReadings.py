from sense_hat import SenseHat
from time import sleep

sense = SenseHat()

# Enables compass
compass_enabled = True

# Every 30 seconds stores magnetometer readings in csv file
with open("magnetometerReadings.csv", "a") as f:
    for i in range(360):
        raw = sense.get_compass_raw()
        f.write(str(raw["x"]) + ", " + str(raw["y"]) + "," + str(raw["z"]) + "\n")
        sleep(30)


f.close()
