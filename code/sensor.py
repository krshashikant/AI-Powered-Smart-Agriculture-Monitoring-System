import random

class Sensor:
    def read_temperature(self):
        return round(random.uniform(20, 40), 1)

    def read_humidity(self):
        return round(random.uniform(40, 90), 1)

    def read_soil_moisture(self):
        return random.randint(20, 100)

    def get_sensor_data(self):
        return {
            "temperature": self.read_temperature(),
            "humidity": self.read_humidity(),
            "soil_moisture": self.read_soil_moisture()
        }


if _name_ == "_main_":
    sensor = Sensor()
    print(sensor.get_sensor_data())
