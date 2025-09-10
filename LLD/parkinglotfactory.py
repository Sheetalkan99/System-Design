import uuid
import time

# -------- VEHICLE CLASSES --------

# Base Vehicle class
class Vehicle:
    def __init__(self, number_plate):
        self.number_plate = number_plate

# Different vehicle types inherit from Vehicle
class Car(Vehicle):
    pass

class Bike(Vehicle):
    pass

class Truck(Vehicle):
    pass


# -------- PARKING SPOT CLASSES --------

# Base class for all parking spots
class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.occupied = False
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        if self.occupied:
            raise Exception("Spot already occupied")
        self.vehicle = vehicle
        self.occupied = True
        print(f"✅ {vehicle.__class__.__name__} assigned to Spot {self.spot_id}")

    def remove_vehicle(self):
        print(f"🚗 Vehicle {self.vehicle.number_plate} removed from Spot {self.spot_id}")
        self.vehicle = None
        self.occupied = False

# Different types of spots for different vehicles
class BikeSpot(ParkingSpot):
    pass

class CarSpot(ParkingSpot):
    pass

class TruckSpot(ParkingSpot):
    pass


# -------- FLOOR CLASS --------

# Each floor contains a list of spots
class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle_type):
        # Return the first matching unoccupied spot
        for spot in self.spots:
            if not spot.occupied and spot.__class__.__name__.startswith(vehicle_type):
                return spot
        return None


# -------- TICKET CLASS --------

class Ticket:
    def __init__(self, vehicle, spot):
        self.ticket_id = str(uuid.uuid4())[:8]  # short random ID
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()

    def calculate_fee(self):
        duration = time.time() - self.entry_time
        rate_per_minute = 10  # example pricing
        return round(duration / 60 * rate_per_minute, 2)


# -------- PARKING LOT MAIN CLASS --------

class ParkingLot:
    def __init__(self):
        self.floors = []
        self.active_tickets = {}

    def add_floor(self, floor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle):
        # Loop through floors to find a matching spot
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle.__class__.__name__)
            if spot:
                spot.assign_vehicle(vehicle)
                ticket = Ticket(vehicle, spot)
                self.active_tickets[ticket.ticket_id] = ticket
                print(f"🎟️ Ticket issued: {ticket.ticket_id}")
                return ticket
        print("❌ No available spots for", vehicle.__class__.__name__)
        return None

    def unpark_vehicle(self, ticket_id):
        if ticket_id not in self.active_tickets:
            print("❌ Invalid Ticket ID")
            return
        ticket = self.active_tickets.pop(ticket_id)
        ticket.spot.remove_vehicle()
        fee = ticket.calculate_fee()
        print(f"💵 Total parking fee: ₹{fee}")


# -------- MAIN TEST CODE --------

if __name__ == "__main__":
    print("🅿️ Starting Parking Lot System...\n")

    # Step 1: Initialize parking lot
    lot = ParkingLot()

    # Step 2: Create floor and add spots
    floor1 = ParkingFloor(1)
    floor1.add_spot(BikeSpot("B1"))
    floor1.add_spot(CarSpot("C1"))
    floor1.add_spot(TruckSpot("T1"))
    lot.add_floor(floor1)

    # Step 3: Park vehicles
    bike = Bike("KA01BP1234")
    car = Car("MH02CP4321")

    ticket1 = lot.park_vehicle(bike)
    ticket2 = lot.park_vehicle(car)

    # Step 4: Simulate time and unpark
    time.sleep(2)  # Wait 2 seconds to simulate parking time

    if ticket1:
        lot.unpark_vehicle(ticket1.ticket_id)

    if ticket2:
        lot.unpark_vehicle(ticket2.ticket_id)
