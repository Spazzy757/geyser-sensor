"""
This class will be used to continually read data from the sensors in there own processes, it will hold functionality to 
get the values from the sensors at any point in time. 
"""
import atexit
from multiprocessing import Process, Value


class SensorController:
    def __init__(self):
        # Global variables for sensors
        self.temp = Value('d', 0)
        self.flow = Value('d', 0)
        self.drip = Value('d', 0)

        # Sensor Reading Processes
        self.check_temp = Process(target=self.temp_sensor, args=(self.temp,))
        self.check_flow = Process(target=self.flow_sensor, args=(self.flow,))
        self.check_drip = Process(target=self.drip_sensor, args=(self.drip,))

        # Start processes
        self.check_temp.start()
        self.check_flow.start()
        self.check_drip.start()

        # Terminates all processes at exit
        atexit.register(self.terminate_processes)

    # This is process checks temperature from the sensor
    @staticmethod
    def temp_sensor(temp):
        # Logic to get temp from sensor goes here
        while True:
            temp.value += 2

    # This process checks the flow from the sensor
    @staticmethod
    def flow_sensor(flow):
        # Logic to get flow from sensor goes here
        while True:
            flow.value += 2

    # This process checks the drip tray sensor
    @staticmethod
    def drip_sensor(drip):
        # Logic to get drip from sensor goes here
        while True:
            drip.value += 2

    # Returns the current flow reading
    def get_flow(self):
        # Logic for converting data goes here
        return self.flow.value

    # Returns the current temperature reading
    def get_temp(self):
        # Logic for converting data goes here
        return self.temp.value

    # Returns current drip value reading
    def get_drip(self):
        # Logic for converting data goes here
        return self.drip.value

    # Terminates all processes
    def terminate_processes(self):
        self.check_temp.terminate()
        self.check_flow.terminate()
        self.check_drip.terminate()
