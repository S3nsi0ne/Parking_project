# data mangling
from datetime import datetime

from Library.bin.qtpy2cpp_lib.astdump import parse_ast
class ParkingSession:

    def __init__(self, car, spot, start_time, end_time, session_id):
        self.car = car
        self.spot = spot
        self.start_time = start_time
        self.end_time = end_time
        self.session_id = session_id

    def session_time(self):
        self.end_time = datetime.now()
        duration = self.end_time - self.start_time
        total_hours = int(duration.total_seconds() / 3600)
        return total_hours

class Parking:

    def __init__(self, name):
        self.owners = []
        self.vehicles = {}
        self.spots = []
        self.subscriptions = {}
        self.name = name
        self.sessions = {}

        # self.session = {
        # 1 : session1,
        # 2 : session2,
        # 3 : session3
        # }

    #

    def enter(self, car):
        # check car registering
        if car.plate in self.vehicles.keys():
            pass
        else:
            print("car not registered")

        if car.is_entered:
            return "car already entered"
        car.is_entered = True

        spot = self.__find_empty_spot()

        # register entering time
        enter_time = datetime.now()
        session1 = ParkingSession(car, spot, enter_time, None, 1)
        self.sessions[session1.session_id] = session1

        # update spot
        spot.update_spot()

    def register_car(self, car):
        if car.plate in self.vehicles.keys():
            print("car already registered")
        else:
            self.vehicles[car.plate] = car

    def __find_empty_spot(self):
        for spot in self.spots:
            if spot.is_empty:
                return spot

    def exit(self, parking_session: ParkingSession):
        # check car in parking
        if not parking_session.car.is_entered:
            return "car not in parking"

        # calculate session time
        session_time = parking_session.session_time()

        # calculate price/cost
        # payment
        # update spot

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



