import uuid
import time

# ------------- Core Models -------------
class Vehicle:
    def __init__(self, number_plate: str):
        self.number_plate = number_plate

class Car(Vehicle): pass
class Bike(Vehicle): pass
class Truck(Vehicle): pass

class ParkingSpot:
    def __init__(self, spot_id: str):
        self.spot_id = spot_id
        self.occupied = False
        self.vehicle = None

    def assign_vehicle(self, vehicle: Vehicle):
        self.vehicle = vehicle
        self.occupied = True

    def remove_vehicle(self):
        self.vehicle = None
        self.occupied = False

class CarSpot(ParkingSpot): pass
class BikeSpot(ParkingSpot): pass
class TruckSpot(ParkingSpot): pass

class ParkingFloor:
    def __init__(self, floor_number: int):
        self.floor_number = floor_number
        self.spots = []  # list[ParkingSpot]

    def add_spot(self, spot: ParkingSpot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle: Vehicle):
        """Very simple rule: Car -> CarSpot, Bike -> BikeSpot, Truck -> TruckSpot."""
        for spot in self.spots:
            if not spot.occupied and (
                (isinstance(vehicle, Car)   and isinstance(spot, CarSpot)) or
                (isinstance(vehicle, Bike)  and isinstance(spot, BikeSpot)) or
                (isinstance(vehicle, Truck) and isinstance(spot, TruckSpot))
            ):
                return spot
        return None

class Ticket:
    def __init__(self, vehicle: Vehicle, spot: ParkingSpot):
        self.ticket_id = str(uuid.uuid4())[:8]
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()  # epoch seconds

    def calculate_fee(self, rate_per_minute: float = 10.0):
        minutes = (time.time() - self.entry_time) / 60.0
        return round(minutes * rate_per_minute, 2)

class ParkingLot:
    def __init__(self):
        self.floors = []                # list[ParkingFloor]
        self.active_tickets = {}        # ticket_id -> Ticket

    def add_floor(self, floor: ParkingFloor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle: Vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle)
            if spot:
                spot.assign_vehicle(vehicle)
                ticket = Ticket(vehicle, spot)
                self.active_tickets[ticket.ticket_id] = ticket
                return ticket
        return None  # no spot available anywhere

    def unpark_vehicle(self, ticket_id: str, rate_per_minute: float = 10.0):
        ticket = self.active_tickets.pop(ticket_id, None)
        if not ticket:
            return None  # invalid ticket
        fee = ticket.calculate_fee(rate_per_minute)
        ticket.spot.remove_vehicle()
        return fee

    def available_summary(self):
        """Returns a simple dict of free spots by type across all floors."""
        counts = {"CarSpot": 0, "BikeSpot": 0, "TruckSpot": 0}
        for floor in self.floors:
            for s in floor.spots:
                if not s.occupied:
                    counts[s.__class__.__name__] += 1
        return counts

# ------------- Tiny Demo -------------
if __name__ == "__main__":
    # Build lot
    lot = ParkingLot()
    f1 = ParkingFloor(1)
    f1.add_spot(CarSpot("C1"))
    f1.add_spot(BikeSpot("B1"))
    f1.add_spot(TruckSpot("T1"))
    lot.add_floor(f1)

    # Park a car
    t = lot.park_vehicle(Car("MH12AB1234"))
    if t:
        print("Ticket:", t.ticket_id, "Spot:", t.spot.spot_id)
    else:
        print("No spot available")

    # ... wait a bit ...
    time.sleep(2)  # 2 seconds

    # Unpark
    fee = lot.unpark_vehicle(t.ticket_id, rate_per_minute=10.0)
    print("Fee:", fee)

    # Availability
    print("Free spots:", lot.available_summary())
