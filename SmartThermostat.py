import bme280
# import requests
import json
from datetime import datetime


class SmartThermostat:

    def __init__(self):
        # Initialize python dictionary with student ID.
        self._value_dic = {"patherId" : ""}
        self._temperature = 0
        self._pressure = 0
        self._humidity = 0

    def set_sensor_readings(self):
        # Gather data from sensors.
        self._temperature, self._pressure, self._humidity = bme280.readBME280All()

    def append_data(self):
        # Appends values to dictionary
        self._value_dic["values"] = [
            {
             "variableName": "Temperature",
             "timeStamp": self._get_current_time(),
             "value": self._temperature
            },
            {
             "variableName": "Pressure",
             "timeStamp": self._get_current_time(),
             "value": self._pressure
            },
            {
             "variableName": "Humidity",
             "timeStamp": self._get_current_time(),
             "value": self._humidity
            }
        ]

    def _get_current_time(self):
        # Grabs time and serializes it.
        local_time = datetime.now()
        return local_time.strftime("%m.%d.%Y %I:%M %p")

    def get_json_data(self):
        # Returns data in JSON format.
        return json.dumps(self._value_dic, indent=2)
