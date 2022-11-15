from tkinter import *
import tkinter as tk

def CreateWindow():
    # declare the window
    window = Tk()
    # set window title
    window.title("CSV System")
    # set window width and height
    window.configure(width=900, height=750)

    window.geometry("900x500")

    #Initialize a Label to display the User Input
    CSVNameLabel = Label(window,text="File Name + Extension:", font=("Courier 14 bold"))
    CSVNameLabel.pack()

    #Create an Entry widget to accept User Input For CSV Name
    CSVNameEntry = Entry(window, width= 40)
    CSVNameEntry.focus_set()
    CSVNameEntry.pack()

    DataLabel = Label(window,text="Data Use (,) Between Values:", font=("Courier 14 bold"))
    DataLabel.pack()

    DataEntry = Entry(window,width=40)
    DataEntry.focus_set()
    DataEntry.pack()

    MyButton1 = Button(text="Submit", width=10)
    MyButton1.pack(side="bottom", pady=6)

    window.mainloop()

CreateWindow()