import time
from SmartThermostat import *


thermo = SmartThermostat()

while(True):

    thermo.set_sensor_readings()
    thermo.append_data()
    payload = thermo.get_json_data()
    # Output test.
    print "Data collected: \n"
    print payload + "\n"

    print "PUT attempt & Response: \n"
    print thermo.send_data("https://10.109.143.88:8443/sendsensorvalue/", payload)

    time.sleep(2)
