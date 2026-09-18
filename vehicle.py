from abc import ABC, abstractmethod

# --------------Vehicle-----------


class Vehicle(ABC):
    def __init__(self, plate, color, owner):
        self.plate = plate
        self.color = color
        self.owner = owner
        self.is_entered = False

    @abstractmethod
    def get_price(self):
        pass


class Car(Vehicle):

    def get_price(self):
        pass


class MotorCycle(Vehicle):

    def get_price(self):
        pass


class Van(Vehicle):

    def get_price(self):
        pass