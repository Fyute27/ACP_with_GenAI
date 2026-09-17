from rental import Vehicle, Renter, ElectricCar, Motorbike


car = Vehicle("Mitsubishi", "Lancer Evolution", "TH9087")

electric_car = ElectricCar("Nissan", "Leaf", "EV7890", 62)

motorbike = Motorbike("Yamaha", "MT-07", "BK2468", 689)

renter = Renter("John", 12345)


print(car)

car.rent()

print(car)

car.return_vehicle()

print(car)


try:
    bad_renter = Renter("", 12345)

except ValueError as e:
    print("Error:", e)


try:
    bad_renter = Renter("Alice", -5)

except ValueError as e:
    print("Error:", e)


vehicles = [car, electric_car, motorbike]

for vehicle in vehicles:
    print(vehicle)