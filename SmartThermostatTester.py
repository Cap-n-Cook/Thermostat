import time
from SmartThermostat import *


thermo = SmartThermostat()

while(True):

    thermo.set_sensor_readings()
    thermo.append_data()
    data = thermo.get_json_data()
    # Output test.
    print data + "\n"
    time.sleep(2)
