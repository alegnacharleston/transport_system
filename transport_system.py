class vehicle(object):
    def __init__(self, name, wheels, engine_type):
        self.name = name
        self.wheels = wheels
        self.engine_type = engine_type

    truck = vehicle()
    car = vehicle()

class truck(vehicle):
    def __init__(self, name):
        self.name = "ford"

    def __init__(self, wheels):
        self.wheels = 4

    def __init__(self, engine_type):
        self.engine_type = "diesel"

class car(vehicle):
    def __init__(self, name):
        self.name = "kia"

    def __init__ (self, engine_type):
        self.engine_type = "gasoline"
