import pyodbc


try:
    connect = pyodbc.connect(r'Driver={Microsoft Access Driver (*.mdb, *.accdb)};DBQ=C:\Users\win10\Dropbox\PC\Documents\Database\Database01.accdb;')
    print("Database is Connected")

    database = connect.cursor()
    database.execute('''INSERT INTO Table1 (ID, FullName, Age, SemGrade, Address)
                    VALUES
                    (11,'Sarah O. Rebulado', 19, 95, 'Cavite')
                    ''')
    database.commit()

    print("Data Added")

except pyodbc.Error:
    print("Error in Connection")