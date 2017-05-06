import atexit
from multiprocessing import Process, Value


class SensorController:
    def __init__(self):
        # Global variables for sensors
        self.temp = Value('d', 0)
        self.flow = Value('d', 1)

        # Sensor Reading Processes
        self.check_temp = Process(target=self.temp_sensor, args=(self.temp,))
        self.check_flow = Process(target=self.flow_sensor, args=(self.flow,))

        # Start processes
        self.check_temp.start()
        self.check_flow.start()

        # Terminates all processes at exit
        atexit.register(self.terminate_processes)

    # This is process checks temperature from the sensor
    @staticmethod
    def temp_sensor(temp):
        # Logic to get temp from sensor goes here
        while True:
            temp.value += 2

    # This is process checks the flow from the sensor
    @staticmethod
    def flow_sensor(flow):
        # Logic to get flow from sensor goes here
        while True:
            flow.value += 2

    # Returns the current flow reading
    def get_flow(self):
        # Logic for converting data goes here
        return self.flow.value

    # Returns the current temperature reading
    def get_temp(self):
        # Logic for converting data goes here
        return self.temp.value

    # Terminates all processes
    def terminate_processes(self):
        self.check_temp.terminate()
        self.check_flow.terminate()
