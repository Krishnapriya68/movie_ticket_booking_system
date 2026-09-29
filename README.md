# Movie Ticket Booking System

A simple beginner-friendly Python project for booking movie tickets.

## About the Project

This project is a menu-driven Movie Ticket Booking System. It was made using basic Python concepts such as functions, lists, dictionaries, JSON file handling, loops, conditions and modular programming.

The project is intentionally kept simple so that a beginner can understand and explain the code.

## Features

- Display movies
- Display available seats
- Book a seat
- Cancel a booking
- Calculate ticket amount
- Display current bookings
- Store data in a JSON file
- Basic validation and testing

## Technologies Used

- Python 3
- JSON
- VS Code
- Git and GitHub

No external Python libraries are required.

## Project Structure

```text
movie_ticket_booking_system/
│
├── main.py
├── movies.py
├── booking.py
├── billing.py
├── data_manager.py
├── utils.py
├── test_project.py
├── statement.md
├── README.md
│
└── data/
    └── movies.json
```

## How to Run

1. Install Python 3.
2. Open this folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python main.py
```

If `python` does not work on Windows, try:

```bash
py main.py
```

## How to Test

Run:

```bash
python test_project.py
```

or:

```bash
py test_project.py
```

The terminal should show:

```text
All tests passed.
```

## Basic Workflow

1. User starts the program.
2. User selects an option from the menu.
3. The program reads movie and booking data.
4. The selected operation is performed.
5. Updated information is saved in `data/movies.json`.
6. The result is displayed to the user.

## Functional Requirements

1. Movie display
2. Available-seat display
3. Seat booking
4. Booking cancellation
5. Ticket amount calculation
6. Booking display

## Non-Functional Requirements

- Usability: simple menu and clear messages
- Reliability: invalid inputs are handled where possible
- Maintainability: code is divided into small files
- Resource efficiency: uses lightweight JSON storage
- Error handling: checks invalid movie, seat and numeric input

## Design

### Architecture

```text
User
  |
  v
main.py
  |
  +----> movies.py
  |
  +----> booking.py
  |          |
  |          v
  |      billing.py
  |
  +----> data_manager.py
              |
              v
       data/movies.json
```

### Workflow

```text
Start
  |
Show Menu
  |
Choose Option
  |
  +--> Display Movies
  |
  +--> Display Seats
  |
  +--> Book Seat --> Save Data
  |
  +--> Cancel --> Save Data
  |
  +--> Calculate Amount
  |
  +--> Display Bookings
  |
  v
Exit
```

## Future Enhancements

- Login system
- Multiple show timings
- Different seat categories
- Graphical user interface
- Real database such as SQLite
- Online payment integration
- Admin panel

## Author

Beginner Python project created for academic learning and demonstration.
