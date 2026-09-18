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
    def __init__(self, spot_id,price):
        super().__init__(spot_id)
        self.price=price
        self.discount={"motor":15,"car":30,"van":45}



class Vip(ParkingSpot):
    def __init__(self, spot_id,price):
        super().__init__(spot_id)
        self.price=price
        self.discount={"motor":25,"car":50,"van":75}


class VipPlus(ParkingSpot):
    def __init__(self, spot_id,price):
        super().__init__(spot_id)
        self.price=price
        self.discount={"motor":30,"car":60,"van":90}