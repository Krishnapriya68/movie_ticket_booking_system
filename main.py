from movies import show_movies, show_available_seats
from booking import book_seat, cancel_booking, show_bookings
from billing import calculate_ticket_amount
from utils import get_positive_integer


def main():
    while True:
        print("\n===== MOVIE TICKET BOOKING SYSTEM =====")
        print("1. Display movies")
        print("2. Display available seats")
        print("3. Book seat")
        print("4. Cancel booking")
        print("5. Calculate ticket amount")
        print("6. Display bookings")
        print("7. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            show_movies()

        elif choice == "2":
            show_available_seats()

        elif choice == "3":
            movie_id = input("Enter movie ID: ").strip()
            seat = input("Enter seat number (example A1): ").strip().upper()
            result = book_seat(movie_id, seat)
            print(result)

        elif choice == "4":
            booking_id = input("Enter booking ID: ").strip().upper()
            print(cancel_booking(booking_id))

        elif choice == "5":
            movie_id = input("Enter movie ID: ").strip()
            quantity = get_positive_integer("Enter number of tickets: ")
            print(calculate_ticket_amount(movie_id, quantity))

        elif choice == "6":
            show_bookings()

        elif choice == "7":
            print("Thank you for using the Movie Ticket Booking System!")
            break

        else:
            print("Please enter a valid choice.")


if __name__ == "__main__":
    main()
