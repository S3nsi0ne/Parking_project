from datetime import datetime
from CW.CW_ParkingProject.parking import Parking, Owner
from CW.CW_ParkingProject.parkingSpot import ParkingSpot, Regular, Vip, VipPlus
from CW.CW_ParkingProject.subscription import Subscription
from CW.CW_ParkingProject.vehicle import MotorCycle, Car, Van


parking1 = Parking("Shahrad_parking")

user1 = Owner("mohammad", 1 , 1239871)
user2 = Owner("Mohadese", 2, 919787655)

motor = MotorCycle("123B12", "black", user1)


car1 = Car("123A12", "green", user1)

car2 = Car("143A12", "yellow", user1)

van1 = Van("123J41", "pink", user2)

spot1 = Regular(1, 20)
spot2 = Vip(2, 40)
spot3 = VipPlus(3, 100)
spot4 = Regular(4, 20)

parking1.add_spot(spot1)
parking1.add_spot(spot2)
parking1.add_spot(spot3)
parking1.add_spot(spot4)

subs1 = Subscription(
    start=datetime(2026, 9, 11, 12, 4, 30),
    end= datetime(2026, 10, 11, 12, 4, 30),
    subscription_id= 1,
)

parking1.register_owner(user1)
parking1.register_owner(user2)

# print(car1)

parking1.register_car(car1)
# print(car2)
parking1.register_car(car2)
# print(motor)
parking1.register_car(motor)
# print(van1)
parking1.register_car(van1)

parking1.add_subscribe(subs1)

session1 = parking1.enter(car1)
parking1.exit(session1, None)
