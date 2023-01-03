def print_menu():
    print("""Choose a number: 
    1. Check slots
    2. Book
    3. Delete a booking
    4. See bookings
    0. QUIT""")

"""
print("Hello, Welcome to your reading list.")
while(True):
    print_menu()
    response = int(input())
    if response == 1:
        print("Here are all of your books")
    elif response == 2:
        print("adding a book")
    elif response == 3:
        print("Deleting a book")
    elif response == 4:
        print("Updating a book")
    else:
        print("Good luck reading!")
        break
"""

import bookingsSDK
from data import Data

print("Hello, Welcome to your COVID Booking.")
while(True):
    print_menu()
    response = int(input())
    if response == 1:
        bookingsSDK.see_slots()
    elif response == 2:
        name = input("Name: " )
        number = input("Aadhar: ")
        date = input("Date: ")
        time = input("Time: ")
        if bookingsSDK.check(date,time):
            bookingsSDK.add(Data(name, number, date, time))
        else:
            print('Slot not available')
    elif response == 3:
        name = input("Name: ")
        number = input("Aadhar: ")
        bookingsSDK.delete_book(Data(name, number, ' ',' '))
    elif response == 4:
        for i in bookingsSDK.get_bookings():
            print(i.name,i.number,i.date,i.time)
    else:
        print("EXITED")
        break