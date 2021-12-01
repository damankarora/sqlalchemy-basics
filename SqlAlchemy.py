from chinook_sqlite import sqlite_chinook
from ctms_er import *

import config as Config

# postgresql://<username>:<password>@<host>/<database>
# Getting url strings secretly.
db_string = Config.DB_URL

userChoice = int(input("Enter 1 for CTMS ER Diagram or 2 for SQLite Chinook: "))

if userChoice == 1:
    ctms_er(db_string)
elif userChoice == 2:
    sqlite_chinook()
else:
    print("Invalid input")
