import csv

def CreateCSV():
    print("")
    fileName = str(input("What would you like to call your CSV file (Include Extension)? "))
    open(fileName, 'wb')