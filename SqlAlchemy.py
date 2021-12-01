from chinook_sqlite import sqlite_chinook
from ctms_er import *

userChoice = int(input("Enter 1 for CTMS ER Diagram or 2 for SQLite Chinook: "))

if userChoice == 1:
    ctms_er()
elif userChoice == 2:
    sqlite_chinook()
else:
    print("Invalid input")
