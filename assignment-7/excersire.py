import random
class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.speed = 0
        self.travelled_distance = 0
    def accelerate(self, change):
        self.speed = max(0, min(self.maximum_speed, self.speed + change))

    def drive(self, hours):
        self.travelled_distance += self.speed * hours
my_car = Car(input("Car registration: "), float(input("Maximum speed: ")))
print("\nCar properties:")
print(my_car.registration_number, my_car.maximum_speed, my_car.speed, my_car.travelled_distance)
print("\nEnter speed changes. Press Enter when finished.")
while True:
    change = input("Speed change (+ to accelerate, - to brake): ")
    if change == "":
        break
    my_car.accelerate(float(change))
print("Current speed:", my_car.speed)
my_car.drive(float(input("How many hours should the car drive? ")))
print("Travelled distance:", my_car.travelled_distance)
number_of_cars = int(input("\nHow many cars in the race? "))
finish_distance = float(input("Race distance in km: "))
cars = [Car("ABC-" + str(i), random.randint(150, 200))
        for i in range(1, number_of_cars + 1)]
hours = 0
while max(car.travelled_distance for car in cars) < finish_distance:
    hours += 1
    for car in cars:
        car.accelerate(random.randint(-10, 15))
        car.drive(1)
print("\nRace finished after", hours, "hours")
print("Registration | Max speed | Current speed | Distance")
for car in cars:
    print(car.registration_number, car.maximum_speed, car.speed,
          round(car.travelled_distance, 2))