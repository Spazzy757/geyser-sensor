"""
This class will handle the logic of checking the current data and calculating any logic required for the data
"""


class Temp:
    @staticmethod
    def check(temp):
        if temp <= 0:
            return True
        else:
            return False
