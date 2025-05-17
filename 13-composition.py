# Engine class
class Engine:
    def start(self):
        print("Engine started!")

# Car class (Composition: Car has an Engine)
class Car:
    def __init__(self, engine):
        self.engine = engine  # yahan composition ho rahi hai

    def start_car(self):
        print("Starting the car...")
        self.engine.start()  # Engine ka method call ho raha hai


# Creating objects
my_engine = Engine()
my_car = Car(my_engine)

# Using the Car class to start the engine
my_car.start_car()
