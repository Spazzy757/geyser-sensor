'''

This Class is for sending information over SigFox network

'''
import atexit
from multiprocessing import Process, Value


class SigFoxController:
    def __init__(self):
        self.counter = Value('d', 0)
        self.send_message_process = Process(target=self.send_message, args=(self.counter,))
        self.send_message_process.start()
        atexit.register(self.terminate_processes)

    @staticmethod
    def send_message(counter):
        while True:
            counter.value += 1

    def get_current_value(self):
        return int(self.counter.value)

    def terminate_processes(self):
        self.send_message_process.terminate()
