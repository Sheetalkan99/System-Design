from enum import Enum
from abc import ABC,abstractmethod
# --------------------- Status(ENUM) ---------------------
class Status(Enum):
    AVAILABLE = "AVAILABLE"
    UNAVAILABLE = "UNAVAILABLE"
    REQUESTED = "REQUESTED"
    COMPLETED = "COMPLETED"
    ONGOING = "ONGOING"
    ACCEPTED = "ACCEPTED"
# --------------------- Vehicle ---------------------
class Vehicle:
    def __init__(self,vehicle_number,model,capacity):
        self.vehicle_number = vehicle_number
        self.model = model
        self.capacity = capacity

    def get_vehicle_info(self):
        print(f"Vehicle Number is {self.vehicle_number}, model is {self.model},capacity is {self.capacity}.")

# --------------------- User ---------------------
class User:
    def __init__(self,name,email,phone):
         self.name = name
         self.email = email
         self.phone = phone
    
    @abstractmethod
    def get_details(self):
        pass

    def __str__(self):
        return f"USER DETAILS: Name: {self.name}, Email: {self.email} and Phone: {self.phone}."
    
# --------------------- Ride ---------------------
class Ride:
    def __init__(self,ride_id,passenger,pick_up,drop):
        self.ride_id = ride_id
        self.passenger = passenger
        self.pick_up = pick_up
        self.drop = drop
        self.driver = None
        self.fare = 0
        self.status = Status.REQUESTED
    
    def assign_driver(self,driver):
        self.driver = driver
        self.status = Status.ACCEPTED
        print(f"Ride {self.ride_id} accepted by Driver {driver.name}")

    def start_ride(self):
        if self.status != Status.ACCEPTED:
            print(f"Cannot start {self.ride_id} as the ride is not Accepted.")
        else:
            self.status = Status.ONGOING
            print(f"{self.ride_id} has started.")

    def end_ride(self):
        if self.status != Status.ONGOING:
            print(f"Ride {self.ride_id} not started, cannot end.")
        else:
            self.status = Status.COMPLETED
            if self.driver:
                self.driver.is_available = Status.AVAILABLE
            print(f"Ride {self.ride_id} ended. Driver {self.driver.name} is now available.")


    def calculate_fare(self,distance):
        self.fare = 10 * distance
        print(f"Ride {self.ride_id} fare: {self.fare}")
        return self.fare
# --------------------- RideManager ---------------------
class RideManager:
    rides = []
    driver = []

    @staticmethod
    def register_driver(driver):
        RideManager.driver.append(driver)
    
    @staticmethod
    def assign_driver(passenger, ride_id, pick_up, drop):
        ride = Ride(ride_id, passenger, pick_up, drop)

        available_driver = None
        for driver in RideManager.driver:
            if driver.is_available == Status.AVAILABLE:
                available_driver = driver
                break
        if available_driver:
            ride.assign_driver(available_driver)
            available_driver.is_avilable = Status.UNAVAILABLE
            print(f"Driver {available_driver.name} assigned to Ride {ride_id}")
        else:
            print(f"No available drivers for Ride {ride_id} at the moment.")
        RideManager.rides.append(ride)
        return ride
    
    @staticmethod
    def show_all_rides():
        print("\nAll Rides:")
        for ride in RideManager.rides:
            driver_name = ride.driver.name if ride.driver else "Not assigned"
            print(f"Ride ID: {ride.ride_id}, Passenger: {ride.passenger.name}, Driver: {driver_name}, Status: {ride.status.value}")

# --------------------- Driver ---------------------
class Driver(User):
    def __init__(self, name, email, phone,driver_id,vehicle,is_available=Status.AVAILABLE):
        super().__init__(name, email, phone)
        self.driver_id = driver_id
        self.vehicle = vehicle
        self.is_available = is_available
    def get_details(self):
        print(f"DRIVER DETAILS: ID: {self.driver_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}, Vehicle: {self.vehicle.model}, Status: {self.is_available.value}")

    def accept_ride(self, ride):
        if self.is_available == Status.AVAILABLE:
            ride.assign_driver(self)
            self.is_available = Status.UNAVAILABLE
            print(f"Driver {self.name} accepted ride {ride.ride_id}")
        else:
            print(f"Driver {self.name} is not available.")

# --------------------- Passenger ---------------------
class Passenger(User):
    def __init__(self, name, email, phone, passenger_id):
        super().__init__(name, email, phone)
        self.passenger_id = passenger_id

    def get_details(self):
        print(f"PASSENGER DETAILS: ID: {self.passenger_id}, Name: {self.name}, Email: {self.email}, Phone: {self.phone}")

    def book_ride(self, ride_id, pick_up, drop):
        print(f"Passenger {self.name} booked a ride {ride_id} from {pick_up} to {drop}")
        return RideManager.assign_driver(self, ride_id, pick_up, drop)

# --------------------- Example Usage ---------------------
# Vehicles
vehicle1 = Vehicle("MH097", "RAV4", 7)
vehicle2 = Vehicle("KA123", "Tesla Model 3", 5)

# Drivers
driver1 = Driver("Bob", "bob@gmail.com", "234567", "D001", vehicle1)
driver2 = Driver("Alice", "alice@gmail.com", "345678", "D002", vehicle2)

RideManager.register_driver(driver1)
RideManager.register_driver(driver2)

# Passengers
passenger1 = Passenger("Cat", "cat@gmail.com", "456789", "P001")
passenger2 = Passenger("Dog", "dog@gmail.com", "567890", "P002")

# Book Rides
ride1 = passenger1.book_ride("R001", "Downtown", "Airport")
ride2 = passenger2.book_ride("R002", "Mall", "Home")

# Ride Lifecycle
ride1.start_ride()
ride1.calculate_fare(15)
ride1.end_ride()

ride2.start_ride()
ride2.calculate_fare(8)
ride2.end_ride()

# Show all rides
RideManager.show_all_rides()

# Driver details after rides
driver1.get_details()
driver2.get_details()

