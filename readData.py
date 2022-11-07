import csv
import os.path

def ReadCSV():
    print("")
    CSVFile = str(input("Enter CSV File Name And Extension: ")) #Reads in CSV File With Input

    file_exists = os.path.exists(CSVFile) # Makes sure file is valid

    while file_exists == False:
        CSVFile = str(input("Re-Enter CSV File Name And Extension: "))
        file_exists = os.path.exists(CSVFile)

    if file_exists == True:
        with open(CSVFile) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            for row in csv_reader:
                print("Reading CSV File Working")
