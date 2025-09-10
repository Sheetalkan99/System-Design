from abc import ABC
from typing import List
from enum import Enum
import uuid

class RideStatus(Enum):
    BOOKED = "Booked"
    ONGOING = "Ongoing"
    COMPLETED = "Completed"
    CANCELED = "Canceled"

class User(ABC):    
    def __init__(self, name, email, phone):
        self.name = name 
        self.email = email 
        self.phone = phone
    def __str__(self):
        return f"Name:{self.name}, Email:{self.email}, Phone:{self.phone}"

class Vehicle:
    def __init__(self,vehicle_number,model,capacity):
        self.vehicle_number = vehicle_number
        self.model = model 
        self.capacity = capacity

    def __str__(self):
        return f"Vehicle[{self.vehicle_number}, {self.model}, Capacity: {self.capacity}]"
        
class Driver(User):
    def __init__(self, name, email, phone, driver_id, vehicle=None, is_available=True):
        super().__init__(name, email, phone)
        self.driver_id = driver_id
        self.vehicle = vehicle
        self.is_available = is_available

    def set_availability(self, availability: bool):
        self.is_available = availability
    
    def assign_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle

    def __str__(self):
        vehicle_info = str(self.vehicle) if self.vehicle else "No vehicle assigned"
        return f"DriverID: {self.driver_id}, {super().__str__()}, Available: {self.is_available}, Vehicle: {vehicle_info}"

class Passenger(User):
    def __init__(self, name, email, phone, passenger_id):
        super().__init__(name, email, phone)
        self.passenger_id = passenger_id
    
    def __str__(self):
        return f"PassengerID: {self.passenger_id}, {super().__str__()}"

class Ride:
    def __init__(self,driver: Driver, passenger: Passenger, pickup:str,drop:str,fare:float):
        self.ride_id = str(uuid.uuid4())
        self.driver = driver
        self.passenger = passenger
        self.pickup = pickup
        self.drop = drop
        self.status = RideStatus.ONGOING
        self.fare = fare
    
    def cancel(self):
        self.status = RideStatus.CANCELED
        self.driver.is_available = True
    
    def completed(self):
        self.status = RideStatus.COMPLETED
        self.driver.is_available = True
    def __str__(self):
        return (f"Ride[{self.ride_id}] | Driver: {self.driver.name}, "
                f"Passenger: {self.passenger.name}, From {self.pickup} → {self.drop}, "
                f"Fare: ${self.fare}, Status: {self.status.value}")
    
class FareCalculator:
    BASE_FARE = 5
    COST_PER_KM = 2

    @staticmethod
    def calculate_fare(distance_km:float):
        return FareCalculator.BASE_FARE + distance_km * FareCalculator.COST_PER_KM

class RideManager:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(RideManager,cls).__new__(cls)
            cls._instance.rides = []
        return cls._instance
    
    @staticmethod
    def get_instance():
        if RideManager._instance is None:
            RideManager._instance = RideManager()
        return RideManager._instance
    
    def assign_driver(self,driver : Driver,passenger : Passenger, pickup,drop,distance):
        if not driver.is_available:
            print(f"Driver {driver.name} is not available.")
            return None
        
        fare = FareCalculator.calculate_fare(distance)
        ride = Ride(driver,passenger,pickup,drop,fare)
        self.rides.append(ride)

        driver.is_available = False
        print(f"Ride Assigned:{ride}")
        return ride
    
    def show_all_rides(self):
        for ride in self.rides:
            print(ride)

    def cancel_ride(self,ride_id):
        for ride in self.rides:
            if ride.ride_id == ride_id:
                ride.cancel()
                print(f"Ride {ride_id} cancelled.")
                return
        print("Ride not found")




if __name__ == "__main__":
    # Vehicles
    v1 = Vehicle("MH12AB1234", "Toyota Innova", 4)
    v2 = Vehicle("MH12XY5678", "Honda City", 4)

    # Drivers (name, email, phone, driver_id, vehicle)
    d1 = Driver("John Doe", "john@example.com", "555-1234", driver_id="D1", vehicle=v1)
    d2 = Driver("Jane Roe", "jane@example.com", "555-5678", driver_id="D2", vehicle=v2)

    # Passengers (name, email, phone, passenger_id)
    p1 = Passenger("Alice Smith", "alice@example.com", "999-1111", passenger_id="P1")
    p2 = Passenger("Bob Brown", "bob@example.com", "999-2222", passenger_id="P2")

    # RideManager (singleton)
    manager = RideManager.get_instance()

    # Assign rides (driver, passenger, pickup, drop, distance)
    r1 = manager.assign_driver(d1, p1, "Pune", "Mumbai", 150)
    r2 = manager.assign_driver(d2, p2, "Delhi", "Noida", 25)

    # Show all rides
    print("\n--- All Rides ---")
    manager.show_all_rides()

    # Cancel one ride
    manager.cancel_ride(r1.ride_id)

    # Show again
    print("\n--- After Cancellation ---")
    manager.show_all_rides()
