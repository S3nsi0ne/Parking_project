#data mangling
from datetime import time
class Parking:
    def enter(self, car):
        #check car registering
        #check car entering...
        spot = self.__find_empty_spot()

        #register entering time
        #update spot


    def register(self, car):
        pass

    def __find_empty_spot(self):
        pass




class Owner:
    pass


class ParkingSession:

    def __init__(self, car, spot, start_time, end_time):
        self.car = car
        self.spot = spot
        self.start_time = start_time
        self.end_time = end_time









