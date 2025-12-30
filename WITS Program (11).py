# WITS Student Manager
# Object oriented GUI program to track student grades and allow user to add and print info on students, courses, and grades
# Developer: Shira Cheifetz
# Date: 12/17/25
import Roster
import gui
from tkinter import *

# Function: main
# Purpose: call the gui app to start the program
# Parameter: none
# Returns: none
def main():
    # if the user has already used the program, retrieve the contents
    studentDict = Roster.Roster.openFile()
    studentRoster = Roster.Roster(studentDict)
    
    # kick off the gui 
    root = Tk()
    root.title("WITS Program")
    root.geometry("500x550")
    app = gui.Application(root, studentRoster)
    root.mainloop()

main()

