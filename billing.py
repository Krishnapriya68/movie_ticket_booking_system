from data_manager import load_data


def calculate_ticket_amount(movie_id, quantity):
    data = load_data()

    for movie in data["movies"]:
        if movie["id"].lower() == movie_id.lower():
            total = movie["price"] * quantity
            return total

    return 0


def show_bill(movie_id, quantity):
    amount = calculate_ticket_amount(movie_id, quantity)

    if amount == 0:
        return "Movie not found."

    return f"Total ticket amount for {quantity} ticket(s): Rs.{amount}"
