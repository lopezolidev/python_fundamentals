class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.has_fuel = False

    def turn_on(self):
        if self.has_fuel:
            print("The car is on")
            return
        print("The car has no fuel")

    def load_with_fuel(self):
        if not self.has_fuel:
            self.has_fuel = True
            print("The car is ready to go")
            return
        print("The car already has fuel")

car_1 = Car("toyota celica", 2022)

print(f"the car is a {car_1.model}, from the year {car_1.year}")
car_1.turn_on()
car_1.load_with_fuel()
car_1.load_with_fuel()
car_1.turn_on()

        
    