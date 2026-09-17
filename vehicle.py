from abc import ABC, abstractmethod

#--------------Vehicle-----------

class Vehicle(ABC):

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