class WaterBottle:
    def __init__(self, color, capacity, volume):
        self.color = color
        self.capacity = capacity
        self.volume = volume

    def drink(self, amount):
        self.volume -= amount
        if self.volume < 0:
            self.volume = 0
    
    def refill(self, amount):
        self.volume += amount
        if self.volume > self.capacity:
            self.volume = self.capacity
    
    # Further Challenges

    def __add__(self, other):
        self.capacity += other.capacity
        self.volume += other.volume
        return self

    def __repr__(self):
        return "A " + self.color + " Waterbottle | Capacity: " + str(self.capacity) + "mL | Volume: " + str(self.volume) + "mL"