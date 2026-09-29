import random


def generate_booking_id():
    return "B" + str(random.randint(1000, 9999))


def get_positive_integer(message):
    while True:
        try:
            number = int(input(message))
            if number > 0:
                return number
            print("Please enter a number greater than 0.")
        except ValueError:
            print("Please enter a valid number.")
