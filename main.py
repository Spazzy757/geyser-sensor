from lib.sigfox.sigfox_controller import SigFoxController
from lib.geyser.sensor_controller import SensorController
import time

sigfox = SigFoxController()
sensor = SensorController()
while True:
    print("++++++++++++++++++++++++++++++++++")
    print('Temp Reading: ', sensor.get_temp())
    print('Flow Reading: ', sensor.get_flow())
    print("++++++++++++++++++++++++++++++++++")
    time.sleep(2)

