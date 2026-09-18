from exceptions import TimeException
from datetime import datetime
# 
class subscription:
    discount = 0.2

    def __init__(self, start, end, status="active"):
        self.start = start
        self.end = end
        self.status = status

    def calculat(self,price,duration):
        today=datetime.now()
        if self.start <= today <= self.end: 
            cost=price * duration * (1-self.discount)
            return cost
        else:
            self.expire()
            print("Your subscription expire")

        



    def renew(self, new_start, new_end):
        if not self.__check_time(new_start, new_end):
            raise TimeException("your end time bigger than start time")
        self.start = new_start
        self.end = new_end

    def cancel(self):
        self.status = "deactive"


    def expire(self):
        self.status = "expired"


    @staticmethod
    def __check_time(start, end):
        if end > start:
            return False
        return True
