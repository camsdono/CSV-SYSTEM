import os 
import csv
from createCSV import CreateCSVName


def WriteCSV():
    fileName = str(input("Enter Filename and file extension: "))
    file_exists = os.path.exists("./CSVFiles/" + fileName)

    if file_exists == False:
        print("")
        print("File does not exist")
        print("1. Would you lile to create a file with that name?")
        print("2. Would you like to return to the menu?")
        print("")
        
        option = int(input("Choose a number between 1 - 2: "))

        while option < 1 or option > 2:
            option = int(input("Invalid choose a number between 1 - 2: "))

        if option == 1:
            print("Creating File...")
            CreateCSVName(fileName)
        if option == 2:
            return

    with open("./CSVFiles/" + fileName, 'a', newline='') as csvfile:
        setRows = int(input("How many rows would you like to add? "))
        dataToInsert = []

        for i in range(setRows):
            dataToInsert.append(input("Enter data to insert: "))

        writer = csv.writer(csvfile)
        writer.writerow(dataToInsert)

        print("")
        print("Data inserted successfully")
            
