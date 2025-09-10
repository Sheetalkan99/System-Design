class Vehicle:
    def start(self):
        pass

    def stop(self):
        pass


class Car(Vehicle):
    def start(self):
        print("Car is starting...")

    def stop(self):
        print("Car is stopping...")


class Truck(Vehicle):
    def start(self):
        print("Truck is starting...")

    def stop(self):
        print("Truck is stopping...")


class Bike(Vehicle):
    def start(self):
        print("Bike is starting...")

    def stop(self):
        print("Bike is stopping...")


# Factory class
class VehicleFactory:
    @staticmethod
    def get_vehicle(vehicle_type):
        vehicle_type = vehicle_type.lower()
        if vehicle_type == "car":
            return Car()
        elif vehicle_type == "truck":
            return Truck()
        elif vehicle_type == "bike":
            return Bike()
        else:
            raise ValueError("Unknown vehicle type")


# Client code
vehicle = VehicleFactory.get_vehicle("truck")
vehicle.start()
vehicle.stop()
