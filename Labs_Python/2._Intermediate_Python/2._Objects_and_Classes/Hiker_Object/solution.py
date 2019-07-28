class Hiker:
    def __init__(self, name, altitude=0, thirst=False):
        self.name = name
        self.altitude = altitude
        self.thirst = thirst

    def climb(self, amount):
        self.altitude += amount
        self.thirst = True
    
    def descend(self, amount):
        self.altitude -= amount
        self.thirst = True

    def drinkbreak(self):
        self.thirst = False