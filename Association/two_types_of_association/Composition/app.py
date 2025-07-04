class Heart:
    def __init__(self):
        print("❤️ Heart created")

    def beat(self):
        print("Heart is beating...")

class Person:
    def __init__(self, name):
        self.name = name
        self.heart = Heart()  # Composition: Person creates and owns Heart

    def live(self):
        print(f"{self.name} is alive.")
        self.heart.beat()

# Create a person object
p1 = Person("Ruba")
p1.live()
