"""
class Vehicle - init
class parkingspot - park(), leave()
class parkinglot - park() , leave(), available_spots()
"""
class Vehicle:
    def __init__(self, license_plate:str):
        self.license_plate = license_plate

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.is_occupied = False
        self.vehicle = None
    
    def park(self, vehicle: Vehicle):
        if not self.is_occupied:
            self.vehicle = vehicle
            self.is_occupied = True
            return True
        return False
    def leave(self):
        if self.is_occupied:
            self.vehicle = None
            self.is_occupied = False
            return True
        return False
class ParkingLot:
    def __init__(self, total_spots: int):
        self.spots = [ParkingSpot(i) for i in range(total_spots)]
    
    def park(self,vehicle: Vehicle):
        for spot in self.spots:
            if not spot.is_occupied:
                spot.park(vehicle)
                return f"Parked at spot {spot.spot_id}"
        return "No available spots"
    def leave(self,spot_id: int):
        if 0 <= spot_id < len(self.spots):
            self.spots[spot_id].leave()
            return f"Vehicle left from spot {spot_id}"
        return "Invalid spot ID"
    def available_spots(self):
        return len([spot for spot in self.spots if not spot.is_occupied])

v1 = Vehicle("ABC123")
v2 = Vehicle("XYZ456")
lot = ParkingLot(5)
print(lot.park(v1))  # Parked at spot 0
print(lot.park(v2))  # Parked at spot 1
print(lot.available_spots())  # 3   