class WaterBottle:
    def __init__(self, color, capacity, volume):
        self.color = color
        self.capacity = capacity
        self.volume = volume

    def drink(amount):
        self.volume -= amount
        if self.volume < 0:
            self.volume = 0
    
    def refill(amount):
        self.volume += amount
        if self.volume > self.capacity:
            self.volume = self.capacity