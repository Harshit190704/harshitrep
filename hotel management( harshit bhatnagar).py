# ------------------------------------------------------
# Hotel Management System - Phase 1 (Interactive Version)
# Name: Harshit Bhatnagar
# Enrollment No: 2402130003
# Date: 27th October 2025
# ------------------------------------------------------

import random

# -------------------------------
# Data Structures
# -------------------------------

rooms = [
    {'room_num': 101, 'type': 'Single', 'price': 1500, 'is_available': True},
    {'room_num': 102, 'type': 'Double', 'price': 2500, 'is_available': True},
    {'room_num': 103, 'type': 'Suite',  'price': 4000, 'is_available': True}
]

guests = {
    'GUEST1001': {
        'name': 'John Doe',
        'room_num': 101,
        'check_in': '2025-10-05'
    }
}

occupied_rooms = {101, 105, 203}

ROOM_TYPES = ('Single', 'Double', 'Suite')

# -------------------------------
# Synchronize Room Availability
# -------------------------------
for room in rooms:
    if room['room_num'] in occupied_rooms:
        room['is_available'] = False


# -------------------------------
# Helper Function: Generate Unique Guest ID
# -------------------------------

def generate_guest_id():
    """Generates a unique guest ID like GUEST1002."""
    while True:
        guest_id = f"GUEST{random.randint(1000, 9999)}"
        if guest_id not in guests:
            return guest_id


# -------------------------------
# Function Definitions
# -------------------------------

def login():
    print("\n[LOGIN FUNCTION]")
    print("Password protection will be added in Phase 2.")
    print("Currently, access is open for all users.")


def add_entry():
    print("\n[ADD ENTRY FUNCTION]")

    name = input("Enter guest name: ")

    # Generate a unique guest ID automatically
    guest_id = generate_guest_id()

    # Display room type options numerically
    print("\nSelect Room Type:")
    for i, rtype in enumerate(ROOM_TYPES, start=1):
        print(f"{i}. {rtype}")

    choice = input("Enter choice (1-3): ").strip()
    if choice not in ('1', '2', '3'):
        print("Invalid choice! Please enter 1, 2, or 3.")
        return

    room_type = ROOM_TYPES[int(choice) - 1]

    # Find available room of that type
    available_room = None
    for room in rooms:
        if room['type'] == room_type and room['is_available']:
            available_room = room
            break

    if not available_room:
        print(f"Sorry, no {room_type} rooms are available right now.")
        return

    check_in = input("Enter check-in date (YYYY-MM-DD): ")

    # Update guest dictionary
    guests[guest_id] = {
        'name': name,
        'room_num': available_room['room_num'],
        'check_in': check_in
    }

    # Update room status
    available_room['is_available'] = False
    occupied_rooms.add(available_room['room_num'])

    print("\n------------------------------------------")
    print(f"Guest {name} added successfully!")
    print(f"Assigned Guest ID: {guest_id}")
    print(f"Assigned Room: {available_room['room_num']} ({room_type})")
    print(f"Check-in Date: {check_in}")
    print("------------------------------------------")


def modify_entry():
    print("\n[MODIFY ENTRY FUNCTION]")
    guest_id = input("Enter Guest ID to modify: ").upper()

    if guest_id not in guests:
        print("Guest not found!")
        return

    print("Current details:", guests[guest_id])
    new_name = input("Enter new name (or press Enter to skip): ")
    new_room = input("Enter new room number (or press Enter to skip): ")

    if new_name:
        guests[guest_id]['name'] = new_name
    if new_room:
        guests[guest_id]['room_num'] = int(new_room)

    print("Guest details updated successfully!")


def delete_entry():
    print("\n[DELETE ENTRY FUNCTION]")
    guest_id = input("Enter Guest ID to delete: ").upper()

    if guest_id not in guests:
        print("Guest not found!")
        return

    room_num = guests[guest_id]['room_num']
    del guests[guest_id]

    # Mark room as available again
    for room in rooms:
        if room['room_num'] == room_num:
            room['is_available'] = True
            break

    if room_num in occupied_rooms:
        occupied_rooms.remove(room_num)

    print(f"Guest record deleted and Room {room_num} is now available.")


def view_report():
    print("\n[VIEW REPORT FUNCTION]")
    print("===== Current Guest List =====")
    if not guests:
        print("No guests found.")
    else:
        for gid, info in guests.items():
            print(f"Guest ID: {gid}, Name: {info['name']}, Room: {info['room_num']}, Check-in: {info['check_in']}")

    print("\n===== Room Status =====")
    for room in rooms:
        status = "Available" if room['is_available'] else "Occupied"
        print(f"Room {room['room_num']} ({room['type']}): {status}")


def search_guest():
    print("\n[SEARCH GUEST FUNCTION]")
    search_name = input("Enter guest name to search: ").lower()
    found = False

    for gid, info in guests.items():
        if info['name'].lower() == search_name:
            print(f"Guest found: {info['name']} | Guest ID: {gid} | Room: {info['room_num']}")
            found = True

    if not found:
        print("No guest found with that name.")


# -------------------------------
# Main Menu Function
# -------------------------------

def main():
    while True:
        print("\n-----------------------------------------------------")
        print("                 HOTEL MANAGEMENT SYSTEM")
        print("-----------------------------------------------------")
        print("2. Add New Guest")
        print("3. Modify Booking")
        print("4. Delete Entry")
        print("5. View Reports")
        print("6. Search Guest")
        print("7. Exit")
        print("-----------------------------------------------------")

        choice = input("Enter your choice (2-7): ").strip()

        if choice == "2":
            add_entry()
        elif choice == "3":
            modify_entry()
        elif choice == "4":
            delete_entry()
        elif choice == "5":
            view_report()
        elif choice == "6":
            search_guest()
        elif choice == "7":
            print("Exiting program. Thank you!")
            break
        else:
            print("Invalid choice! Please enter a number between 2 and 7.")

        input("\nPress Enter to continue...")


# -------------------------------
# Run the Program
# -------------------------------
if __name__ == "__main__":
    main()
