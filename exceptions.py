class TimeException(Exception):
    pass


class ParkingException(Exception):
    pass


class DuplicatePlate(ParkingException):
    pass

class ExitingInParking(ParkingException):
    pass

class NoneExistingInParking(ParkingException):
    pass

class InvalidSpot(ParkingException):
    pass

class InvalidSubscription(Exception):
    pass

