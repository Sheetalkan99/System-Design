from enum import Enum
from abc import ABC,abstractmethod
class Status(Enum):
    REGULAR = "regular"
    PREMIUM = "premium"
    CONFIRMED = "confirmed"
    CANCELLED = "cancelled"

class Movie:
    def __init__(self,movie_id,title,duration_minutes,genre):
        self.movie_id = movie_id
        self.title = title
        self.duration_minutes = duration_minutes
        self.genre = genre
    
    def get_movie_info(self):
        print(f"Movie Details \n Movie ID: {self.movie_id}, Title:{self.title},Duration:{self.duration_minutes}, Genre:{self.genre}")

class Theater:
    def __init__(self,theater_id,name,total_seats):
        self.theater_id = theater_id
        self.name = name
        self.total_seats = total_seats

    def get_theater_info(self):
        print(f"Theater Details: \n Theater ID: {self.theater_id}, Theater Name:{self.name},Total Seats:{self.total_seats}.")     

class Show:
    def __init__(self,show_id,movie,theater:Theater,time):
        self.show_id = show_id
        self.movie = movie
        self.theater = theater
        self.available_seats = {Status.REGULAR: 50, Status.PREMIUM: 20}
        self.time = time

    def get_show_info(self):
        print(f"Show Details:\n Show ID: {self.show_id}, Movie: {self.movie.title}, Theater: {self.theater.name}, Time: {self.time}")
        print("\n Available Seats:")
        for category, seats in self.available_seats.items():
            print(f"{category.value}: {seats}")
    
    def book_seats(self,category:str,seats:int):
        category_enum = Status(category.lower())
        if self.available_seats.get(category_enum,0) >= seats:
            self.available_seats[category_enum] -= seats
            print(f"********************************************************")
            print(f"Booked for {seats} seats for \n Details:\n Show ID: {self.show_id}, Movie: {self.movie.title}, Theater: {self.theater.name}, Time: {self.time}")
            return True
        else:
            print(f"Not Enough Seats Available!")
            return False

class User(ABC):

    def __init__(self,name,email,phone):
        self.name = name
        self.email = email
        self.phone = phone

    @abstractmethod
    def get_details(self):
        pass        

class Customer(User):
    def __init__(self, name, email, phone):
        super().__init__(name, email, phone)
        self.booking_history = []

    def get_details(self):
        print(f"Customer details:\n Name:{self.name}, Email:{self.email}, Phone : {self.phone}")

    def book_ticket(self,show:'Show',seats:int,category:Status):
        booking = BookingManager.create_booking(self,show,seats,category)
        if booking:
            self.booking_history.append(booking)

class Booking:
    FARE = {
        Status.REGULAR: 15,
        Status.PREMIUM: 30
    }

    def __init__(self, booking_id, customer: Customer, show: Show, seats_booked, category: Status):
        self.booking_id = booking_id
        self.customer = customer
        self.show = show
        self.seats_booked = seats_booked
        self.category = category
        self.status = Status.CONFIRMED

    def calculate_fare(self):
        return self.FARE[self.category] * self.seats_booked

    def __str__(self):
        return f"Booking[{self.booking_id}] - {self.customer.name} booked {self.seats_booked} {self.category.value} seats for {self.show.movie.title} at {self.show.theater.name}, Fare = ${self.calculate_fare()}"

    
class BookingManager:
    bookings = []
    booking_counter = 1

    @classmethod
    def create_booking(cls,customer:Customer,show:Show,seats:int,category:Status):
        if not show.book_seats(category.value,seats):
            return None
        booking_id = f"B{cls.booking_counter}"
        cls.booking_counter += 1

        booking = Booking(booking_id,customer,show,seats,category)
        cls.bookings.append(booking)
        print(f"Booking created: {booking}")
        return booking

    def cancel_booking():
        pass
    def show_all_booking():
        pass
    def get_customer_booking():
        pass


# Create movie and theater
movie1 = Movie("123","Toy Story","220","Fiction")
movie1.get_movie_info()        

theater1 = Theater("1","INOX","100")
theater1.get_theater_info()

# Create show
show1 = Show("S1", movie1, theater1, "2025-08-21 18:00")
show1.get_show_info()

# Test booking seats directly from Show
show1.book_seats("regular", 10)  # Should succeed
show1.book_seats("premium", 25)  # Should fail (only 20 premium seats)

# Create a customer and book via BookingManager
customer1 = Customer("Alice", "alice@email.com", "123456789")
customer1.book_ticket(show1, 5, Status.REGULAR)  # BookingManager will handle
customer1.book_ticket(show1, 30, Status.PREMIUM) # Should fail

# Check updated show info
show1.get_show_info()

# Check customer's booking history
print("\nCustomer Booking History:")
for booking in customer1.booking_history:
    print(f"Booking ID: {booking.booking_id}, Customer: {booking.customer.name}, "
          f"Show: {booking.show.show_id}, Seats: {booking.seats_booked}, "
          f"Category: {booking.category.value}, Fare: ${booking.calculate_fare()}")


