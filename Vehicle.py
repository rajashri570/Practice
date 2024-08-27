class Vehicle:
    def __init__(self):
        self.name = None
        self.mileage = None
        self.capacity = None
        return self
class Bus(Vehicle):
    def __init__(self):
        self.name = 'Bus'
        self.mileage = 12
        self.capacity = 50