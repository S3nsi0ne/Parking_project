# data mangling
from datetime import time


class Parking:

    def __init__(self, name):
        self.owners = []
        self.vehicles = {}
        self.spots = []
        self.subscriptions = []
        self.name = name
# 


    def enter(self, car):
        # check car registering
        # check car entering...
        spot = self.__find_empty_spot()

        # register entering time
        # update spot

    def register_car(self, car):
        # find car
        pass

    def __find_empty_spot(self):
        pass

    def exit(self):
        # check car in parking
        # calculate session time
        # calculate price/cost
        # payment
        # update spot
        pass

    def __check_car_in_parking(self):
        pass

    def calculate(self):
        # time - price - discount - spot
        pass

    def payment(self):
        pass

    def register_owner(self):
        pass

    def edit_owner(self):
        pass

    def add_spot(self):
        pass

    def change_spot_id(self):
        pass

    def change_spot(self):
        pass

    def show_all_car_in_parking(self):
        pass


class Owner:

    def __init__(self, name, owner_id, phone_number):
        self.name = name
        self.owner_id = owner_id
        self.phone_number = phone_number
        self.car = []

    def add_car(self, car):
        pass

    def remove_car(self, car):
        pass


class ParkingSession:

    def __init__(self, car, spot, start_time, end_time,session_id):
        self.car = car
        self.spot = spot
        self.start_time = start_time
        self.end_time = end_time
        self.session_id = session_id

    def session_time(self):
        pass








