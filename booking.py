from data_manager import load_data, save_data
from billing import calculate_ticket_amount
from utils import generate_booking_id


def find_movie(data, movie_id):
    for movie in data["movies"]:
        if movie["id"].lower() == movie_id.lower():
            return movie
    return None


def book_seat(movie_id, seat):
    data = load_data()
    movie = find_movie(data, movie_id)

    if movie is None:
        return "Movie not found."

    if seat not in movie["seats"]:
        return "Invalid seat number."

    if seat in movie["booked_seats"]:
        return "This seat is already booked."

    movie["booked_seats"].append(seat)

    booking_id = generate_booking_id()
    amount = calculate_ticket_amount(movie_id, 1)

    data["bookings"].append({
        "booking_id": booking_id,
        "movie_id": movie["id"],
        "movie_name": movie["name"],
        "seat": seat,
        "amount": amount
    })

    save_data(data)

    return (
        f"Booking successful!\n"
        f"Booking ID: {booking_id}\n"
        f"Movie: {movie['name']}\n"
        f"Seat: {seat}\n"
        f"Amount: Rs.{amount}"
    )


def cancel_booking(booking_id):
    data = load_data()

    for booking in data["bookings"]:
        if booking["booking_id"].upper() == booking_id.upper():
            movie = find_movie(data, booking["movie_id"])

            if movie and booking["seat"] in movie["booked_seats"]:
                movie["booked_seats"].remove(booking["seat"])

            data["bookings"].remove(booking)
            save_data(data)
            return "Booking cancelled successfully."

    return "Booking ID not found."


def show_bookings():
    data = load_data()

    print("\n----- CURRENT BOOKINGS -----")

    if not data["bookings"]:
        print("No bookings found.")
        return

    for booking in data["bookings"]:
        print(
            f'{booking["booking_id"]} | '
            f'{booking["movie_name"]} | '
            f'Seat: {booking["seat"]} | '
            f'Rs.{booking["amount"]}'
        )
