from data_manager import load_data


def show_movies():
    data = load_data()

    print("\n----- AVAILABLE MOVIES -----")
    for movie in data["movies"]:
        print(
            f'{movie["id"]}. {movie["name"]} | '
            f'Language: {movie["language"]} | '
            f'Ticket: Rs.{movie["price"]}'
        )


def show_available_seats():
    data = load_data()

    print("\n----- AVAILABLE SEATS -----")
    for movie in data["movies"]:
        available = [
            seat for seat in movie["seats"]
            if seat not in movie["booked_seats"]
        ]
        print(f'{movie["id"]}. {movie["name"]}')
        print("Available:", ", ".join(available))
