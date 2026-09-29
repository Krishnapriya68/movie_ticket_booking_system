from billing import calculate_ticket_amount
from booking import book_seat, cancel_booking
from data_manager import load_data, save_data


def reset_data():
    data = load_data()
    for movie in data["movies"]:
        movie["booked_seats"] = []
    data["bookings"] = []
    save_data(data)


def test_ticket_amount():
    assert calculate_ticket_amount("M1", 2) == 300


def test_booking_and_cancellation():
    reset_data()

    result = book_seat("M1", "A1")
    assert "Booking successful!" in result

    data = load_data()
    assert "A1" in data["movies"][0]["booked_seats"]

    booking_id = data["bookings"][0]["booking_id"]
    assert "successfully" in cancel_booking(booking_id).lower()

    data = load_data()
    assert "A1" not in data["movies"][0]["booked_seats"]


if __name__ == "__main__":
    test_ticket_amount()
    test_booking_and_cancellation()
    print("All tests passed.")
