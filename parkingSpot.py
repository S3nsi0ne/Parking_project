class ParkingSpot:
    def __init__(self, spot_id):
        self.is_active = True
        self.is_empty = False
        self.spot_id = spot_id

    def update_spot(self):
        if self.is_empty:
            self.is_empty = False
        else:
            self.is_empty = True


class Regular(ParkingSpot):
    pass


class Vip(ParkingSpot):
    pass


class VipPlus(ParkingSpot):
    pass