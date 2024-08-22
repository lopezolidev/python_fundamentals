#vehicle object
class Vehicle:
    def __init__(self, model, year, price):
        self.model = model
        self.year = year
        self.price = int(price)
        self.is_sold = True
    #constructor object for a car

    def sell_car(self, client):
        if client.balance >= self.price:
            client.balance -= self.price
            self.is_sold = False
            print(f"The car {self.model} {self.year} has been sold to {client.name}\n")
            return
        print(f"Sorry {client.name}, you cannot buy {self.model} {self.year} for {client.balance}$\n") 
    #method for selling a car    

#User code
class User:
    def __init__(self, name, balance):
        self.name = name
        self.balance = int(balance)
        self.cars = []

#Concessionary code
class Concessionary:
    def __init__(self, name):
        self.name = name
        self.clients = []
        self.vehicles = []

    def show_vehicles(self):
        for vehicle in self.vehicles:
            print(f"{vehicle.model} {vehicle.year} \n")


    def show_clients(self):
        for client in self.clients:
            print(f"{client.name} \n")

    def sell_vehicle(self, client, vehicle):
        if client in self.clients and vehicle in self.vehicles:
            self.vehicles.remove(vehicle)
            vehicle.sell_car(client)
            return
        print(f"The person {client.name} or the car {vehicle.model} are not in our data bases")

    def register_client(self, client):
        if client not in self.clients:
            self.clients.append(client)
            print(f"The client {client.name} has been added to the clients data base")
            return
        print(f"The client {client.name} is already in our data base")

    def register_vehicle(self, vehicle):
        if vehicle not in self.vehicles:
            self.vehicles.append(vehicle)
            print(f"The car {vehicle.model} has been added to the vehicles data base")
            return
        print(f"The car {vehicle.model} is already in our data base")


#creating vehicles
vehicle_1 = Vehicle("Toyota Celica", 2022, 6000)
vehicle_2 = Vehicle("Ford Explorer", 2024, 15000)
vehicle_3 = Vehicle("Chevrolet Camaro", 2020, 18000)

# creating users
user_1 = User("John Doe", 7000)
user_2 = User("Mary Ann", 20000)

# Creating concessionary

concessionary_1 = Concessionary("Pete's cars")
concessionary_1.sell_vehicle(user_1, vehicle_2)

concessionary_1.register_client(user_1)

concessionary_1.register_client(user_1)

concessionary_1.register_vehicle(vehicle_1)

concessionary_1.register_vehicle(vehicle_1)

concessionary_1.register_client(user_2)

concessionary_1.register_vehicle(vehicle_2)
concessionary_1.register_vehicle(vehicle_3)

concessionary_1.sell_vehicle(user_1, vehicle_1)
concessionary_1.sell_vehicle(user_2, vehicle_2)

print(concessionary_1.show_clients())
print(concessionary_1.show_vehicles())

