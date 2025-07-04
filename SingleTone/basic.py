class Singleton:
    _instance = None  # Class-level variable to store single instance

    def __new__(cls):
        # IF instance is not make, then make
        if cls._instance is None:
            print("Creating the Singleton instance...")
            cls._instance = super(Singleton, cls).__new__(cls)
        return cls._instance

    def __init__(self):
        print("Initializing Singleton (but only once)")

# Test the Singleton
s1 = Singleton()
s2 = Singleton()

print(s1 is s2)  # True: Both are same instance
