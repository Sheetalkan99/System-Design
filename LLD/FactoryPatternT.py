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


# Traditional approach: create objects manually
vehicle1 = Car()
vehicle2 = Truck()
vehicle3 = Bike()

vehicle1.start()
vehicle2.start()
vehicle3.start()
