"""
This Class is for sending information over SigFox network, a process will be started that will collect data
every ten minutes and send it to a sigfox connection
"""
import atexit
from multiprocessing import Process, Value


class SigFoxController:
    # Initialization of controller
    def __init__(self):
        self.counter = Value('d', 0)
        self.send_message_process = Process(target=self.send_message, args=(self.counter,))
        self.send_message_process.start()
        atexit.register(self.terminate_processes)

    # This process will run separately and send a message every 10 mins
    @staticmethod
    def send_message(counter):
        while True:
            counter.value += 1

    # This function terminates all functions at exit
    def terminate_processes(self):
        self.send_message_process.terminate()
