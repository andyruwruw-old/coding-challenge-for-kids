# Base Challenge

wb1 = WaterBottle("Blue", 100, 50)
print(wb1.color, str(wb1.capacity), str(wb1.volume))
wb1.drink(25)
print(wb1.color, str(wb1.capacity), str(wb1.volume))
wb1.drink(50)
print(wb1.color, str(wb1.capacity), str(wb1.volume))
wb1.refill(50)
print(wb1.color, str(wb1.capacity), str(wb1.volume))
wb1.refill(200)
print(wb1.color, str(wb1.capacity), str(wb1.volume))

# Further Challenge

wb1 = WaterBottle("Blue", 100, 50)
print(wb1)
wb2 = WaterBottle("Blue", 200, 25)
print(wb2)
wb3 = wb1 + wb2
print(wb3)