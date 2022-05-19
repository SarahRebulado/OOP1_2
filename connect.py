import pyodbc

try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\win10\Dropbox\PC\Documents\Database\Database01.accdb;')
    print("Database is Connected")

except pyodbc.Error:
    print("Error in Connection")
