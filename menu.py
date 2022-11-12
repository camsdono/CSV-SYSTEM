from createCSV import CreateCSV
from readData import ReadCSV
from writeCSV import WriteCSV

print("PYTHON CSV MENU")
#xlsx 

def Menu():
    print("")

    print("1. Create CSV File")
    print("2. Write To CSV File")
    print("3. Read CSV File")
    print("4. Exit")

    option = int(input("Select a number between 1-4: "))

    while option < 1 or option > 4:
        option = int(input("Try again select a number between 1-4: "))

    if option == 1:
        CreateCSV()
        Menu()

    if option == 2:
        WriteCSV()
        Menu()

    if option == 3:
        ReadCSV()
        Menu()
        
    if option == 4:
        return

Menu()

#23A 23B - Seat numbers plane EGPH - EGLC