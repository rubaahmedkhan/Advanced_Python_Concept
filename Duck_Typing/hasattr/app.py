class Cat:
    def meow(self):
        print("MEOW!")

cat = Cat()

print(hasattr(cat, "meow"))       #   True

print(hasattr(cat, "bark"))        # False