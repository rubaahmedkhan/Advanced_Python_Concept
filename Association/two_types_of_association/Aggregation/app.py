class Engine:
    def __init__(self, horsepower):
        self.horsepower = horsepower

    def start(self):
        print(f"Engine with {self.horsepower} HP is starting...")

class Car:
    def __init__(self, model, engine):
        self.model = model
        self.engine = engine  # Aggregation: Car "has-a" Engine

    def drive(self):
        print(f"{self.model} is driving.")
        self.engine.start()

# Create an Engine object
engine1 = Engine(200)

# Create a Car object with engine1
car1 = Car("Toyota Corolla", engine1)

# Use car1
car1.drive()
