import csv
import os

def CreateCSV():
    print("")
    fileName = str(input("What would you like to call your CSV file (Include Extension)? "))
    file_exists = os.path.exists("./CSVFiles/" + fileName)

    while file_exists == True:
        fileName = str(input("File already exists try again. What would you like to call your CSV file (Include Extension)? "))
        file_exists = os.path.exists("./CSVFiles/" + fileName)

    if file_exists == False:
        open("./CSVFiles/" + fileName, 'wb')

def CreateCSVName(fileName):
    file_exists = os.path.exists("./CSVFiles/" + fileName)

    while file_exists == True:
        fileName = str(input("File already exists try again. What would you like to call your CSV file (Include Extension)? "))
        file_exists = os.path.exists("./CSVFiles/" + fileName)

    if file_exists == False:
        open("./CSVFiles/" + fileName, 'wb')
        print("File Created")