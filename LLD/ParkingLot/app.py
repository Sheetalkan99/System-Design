from flask import Flask, render_template, request, redirect, url_for
import uuid
import time

app = Flask(__name__)

# ------------------ Core Classes ------------------
class Vehicle:
    def __init__(self, number_plate):
        self.number_plate = number_plate

class Car(Vehicle): pass
class Bike(Vehicle): pass
class Truck(Vehicle): pass

class ParkingSpot:
    def __init__(self, spot_id):
        self.spot_id = spot_id
        self.occupied = False
        self.vehicle = None

    def assign_vehicle(self, vehicle):
        self.vehicle = vehicle
        self.occupied = True

    def remove_vehicle(self):
        self.vehicle = None
        self.occupied = False

class CarSpot(ParkingSpot): pass
class BikeSpot(ParkingSpot): pass
class TruckSpot(ParkingSpot): pass

class ParkingFloor:
    def __init__(self, floor_number):
        self.floor_number = floor_number
        self.spots = []

    def add_spot(self, spot):
        self.spots.append(spot)

    def find_available_spot(self, vehicle_type):
        for spot in self.spots:
            if not spot.occupied and spot.__class__.__name__.startswith(vehicle_type):
                return spot
        return None

class Ticket:
    def __init__(self, vehicle, spot):
        self.ticket_id = str(uuid.uuid4())[:8]
        self.vehicle = vehicle
        self.spot = spot
        self.entry_time = time.time()

    def calculate_fee(self):
        return round((time.time() - self.entry_time) / 60 * 10, 2)

class ParkingLot:
    def __init__(self):
        self.floors = []
        self.active_tickets = {}

    def add_floor(self, floor):
        self.floors.append(floor)

    def park_vehicle(self, vehicle):
        for floor in self.floors:
            spot = floor.find_available_spot(vehicle.__class__.__name__)
            if spot:
                spot.assign_vehicle(vehicle)
                ticket = Ticket(vehicle, spot)
                self.active_tickets[ticket.ticket_id] = ticket
                return ticket
        return None

    def unpark_vehicle(self, ticket_id):
        ticket = self.active_tickets.pop(ticket_id, None)
        if ticket:
            ticket.spot.remove_vehicle()
            return ticket.calculate_fee()
        return None

# ------------------ App Initialization ------------------
parking_lot = ParkingLot()
floor1 = ParkingFloor(1)
floor1.add_spot(CarSpot("C1"))
floor1.add_spot(BikeSpot("B1"))
floor1.add_spot(TruckSpot("T1"))
parking_lot.add_floor(floor1)

# ------------------ Flask Routes ------------------
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/park', methods=['GET', 'POST'])
def park():
    if request.method == 'POST':
        v_type = request.form['vehicle_type']
        plate = request.form['number_plate']
        vehicle = {'Car': Car, 'Bike': Bike, 'Truck': Truck}[v_type](plate)
        ticket = parking_lot.park_vehicle(vehicle)
        if ticket:
            return render_template('ticket.html', ticket=ticket)
        return "No available spot."
    return render_template('park.html')

@app.route('/unpark', methods=['GET', 'POST'])
def unpark():
    if request.method == 'POST':
        ticket_id = request.form['ticket_id']
        fee = parking_lot.unpark_vehicle(ticket_id)
        if fee is not None:
            return f"Vehicle unparked. Total Fee: ₹{fee}"
        return "Invalid ticket ID."
    return render_template('unpark.html')

if __name__ == '__main__':
    app.run(debug=True)
