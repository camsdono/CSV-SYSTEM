from createCSV import CreateCSV
from readData import ReadCSV

print("PYTHON CSV MENU")

def Menu():
    print("")

    print("1. Create CSV File")
    print("2. Read CSV File")
    print("3. Write To CSV File")
    print("4. Exit")

    option = int(input("Select a number between 1-3: "))

    while option < 1 or option > 3:
        option = int(input("Try again select a number between 1-3: "))

    if option == 1:
        CreateCSV()
        Menu()

    if option == 2:
        ReadCSV()
        Menu()
        #23A 23B

Menu()