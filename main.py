from controller.sigfox.sigfox_controller import SigFoxController
from controller.geyser.sensor_controller import SensorController
from controller.geyser.geyser_controller import GeyserController
from controller.geyser.checks.check import Temp
import time

# Starts instance of SigFox Controller
sigfox = SigFoxController()

# Starts instance of Sensor Controller
sensor = SensorController()
geyser = GeyserController()

# Analyze data classes
temp = Temp()

while True:
    print("++++++++++++++++++++++++++++++++++")
    print("Temp Reading: ", sensor.get_temp())
    print("Flow Reading: ", sensor.get_flow())
    print("Status of Temp", temp.check(sensor.get_temp()))
    if sensor.get_temp() is False:
        geyser.turn_off_power()
    print("++++++++++++++++++++++++++++++++++")
    time.sleep(2)

