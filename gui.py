# Application module
# creates gui widgets
# Developer: Shira Cheifetz
# Date: 12/25/25

import os
from tkinter import *
from tkinter import ttk
from tkinter import messagebox


# Application Class
# creates widgets
class Application(Frame):
    # constructor
    def __init__(self, master, studentRoster):
        super(Application, self).__init__(master)
        self.studentRoster = studentRoster
        self.grid()
        self.createWidgets()


    # Function: createWidgets
    # displays menu options
    # Parameters: none
    # returns: none
    def createWidgets(self):
        # Menu Label
        self.menuLabel = ttk.Label(self, text="WITS Program - Menu Options:", font=('Arial', 12, 'bold'))
        self.menuLabel.grid(row= 0, column= 0, sticky= 'w', padx= 10, pady= 10)
        # ADD STUDENTS
        self.btn1 = ttk.Button(self, text= "Add Students", width= 30, command= self.addStudentsDisplay)
        self.btn1.grid(row= 1, column= 0, sticky= 'w', padx= 2, pady= 2)
        # ADD COURSE
        self.btn2 = ttk.Button(self, text= "Add courses and grades", width= 30, command= self.addCourseDisplay)
        self.btn2.grid(row= 2, column= 0, sticky= 'w', padx= 2, pady= 2)
        # LIST STUDENTS
        self.btn3 = ttk.Button(self, text= "List all students", width= 30, command= self.listStudentsDisplay)
        self.btn3.grid(row= 3, column= 0, sticky= 'w', padx= 2, pady= 2)
        # LOOK UP GRADE
        self.btn4 = ttk.Button(self, text= "Look up a student grade", width= 30, command= self.lookUpDisplay)
        self.btn4.grid(row= 4, column= 0, sticky= 'w', padx= 2, pady= 2)
        # ADD COMMENT
        self.btn5 = ttk.Button(self, text= "Add a comment", width= 30, command= self.addCommentDisplay)
        self.btn5.grid(row= 5, column= 0, sticky= 'w', padx= 2, pady= 2)
        # SAVE REPORT CARD
        self.btn6 = ttk.Button(self, text= "Save a report card", width= 30, command= self.saveReportCardDisplay)
        self.btn6.grid(row= 6, column= 0, sticky= 'w', padx= 2, pady= 2)
        # SAVE TRANSCRIPT
        self.btn7 = ttk.Button(self, text= "Save a transcript", width= 30, command= self.saveTranscriptDisplay)
        self.btn7.grid(row= 7, column= 0, sticky= 'w', padx= 2, pady= 2)
        # EXIT
        self.btn8 = ttk.Button(self, text= "Exit", width= 30, command= self.exitProgram)
        self.btn8.grid(row= 8, column= 0, sticky= 'w', padx= 2, pady= 2)

        # create every widget without gridding any
        self.choiceLabel = ttk.Label(self, text = "Select an option to add students: ")
        self.enterFmt = StringVar()
        self.enterFmt.set(None)
        self.manualRadioBtn = ttk.Radiobutton(self, text = "Enter manually", variable = self.enterFmt, value = "enter manually", command = self.enterManuallyDisplay)
        self.fileRadioBtn = ttk.Radiobutton(self, text = "Load from a text file", variable = self.enterFmt, value = "load text file", command = self.fileUploadDisplay)
        self.studentLbl = ttk.Label(self, text= "Enter student name:")
        self.studentEntry= ttk.Entry(self)
        self.submitNameButton = ttk.Button(self, text = "Submit", command = self.submitStudent)
        self.fileNameLbl = ttk.Label(self, text= "Enter file name and click to submit: ")
        self.enterFileName = ttk.Entry(self)
        self.submitFileBtn = ttk.Button(self, text = "Submit", command = self.uploadFile)
        self.courseLbl = ttk.Label(self, text = "Enter course name: ")
        self.courseEntry = ttk.Entry(self)
        self.gradeLbl = ttk.Label(self, text= "Enter letter grade received in the course: ")
        self.gradeEntry = ttk.Entry(self)
        self.submitGradeBtn = ttk.Button(self, text= "Submit", command= self.submitGrade)
        self.commentLbl = ttk.Label(self, text= "Enter comment (optional):")
        self.commentBox = Text(self, width= 28, height= 9, wrap= "word")
        self.listStudentsText = Text(self, width = 35, height = 14, wrap = "word")
        self.courseLbl = ttk.Label(self, text = "Enter course name: ")
        self.courseEntry = ttk.Entry(self)
        self.submitCourseBtn = ttk.Button(self, text= "Submit", command= self.lookUpInfo)
        self.courseLbl = ttk.Label(self, text = "Enter course name:")
        self.courseEntry = ttk.Entry(self)
        self.commentLbl = ttk.Label(self, text= "Enter comment:")
        self.commentBox = Text(self, width= 28, height= 9, wrap= "word")
        self.submitCommentBtn = ttk.Button(self, text= "Submit", command= self.addCommentInfo)
        self.saveReportCardBtn = ttk.Button(self, text= "Save", command= self.saveReportCard)
        self.semesterLbl = ttk.Label(self, text= "Select a semester: ")
        semesters = ["Spring 2025", "Fall 2025", "Spring 2026", "Fall 2026"] # List of semester options
        self.chosenSemester = StringVar()
        self.dropDown = ttk.Combobox(self, textvariable= self.chosenSemester, values= semesters, state='readonly') # creates dropdown menu
        self.saveTranscriptBtn = ttk.Button(self, text= "Save", command= self.saveTranscript)


    # Function: clearRows
    # "forgets" all widget placements in the specified rows
    # Parameters: int startRow and endRow (default values because it's always the same rows)
    # returns: none
    def clearRows(self, startRow = 9, endRow = 18):
        # Get all widgets managed by the grid in this frame
        for widget in self.grid_slaves():
            info = widget.grid_info() # Check the grid info for each widget
            # if the widget's row is within the range
            if startRow <= int(info.get("row", -1)) <= endRow:
                widget.grid_forget()


    # Function: addStudentsDisplay
    # User chooses if they want to add students manually or load from a text file
    # Parameter: none
    # Returns: none
    def addStudentsDisplay(self):
        self.clearRows()
        # change directory to directory of current script            
        os.chdir(os.path.dirname(os.path.realpath(__file__)))
        self.choiceLabel.grid(row = 9, column = 0, sticky = 'w')
        self.manualRadioBtn.grid(row = 10, column = 0, sticky = 'w')
        self.fileRadioBtn.grid(row = 11, column = 0, sticky = 'w')


    # Function: enterManuallyDisplay
    # enter a new student display
    # parameters: none
    # returns: none
    def enterManuallyDisplay(self):
        self.clearRows()
        self.gridStudentWidgets()
        # self.studentID_lbl.grid(row= 10, column= 0, sticky= 'w')
        # self.enterID.grid(row= 10, column= 1, sticky= 'w')
        self.submitNameButton.grid(row = 9, column = 2, sticky = 'w')
    

    # Function: submitStudent
    # get student name and pass it to addIndividualStudent in the Roster module
    # parameters: none
    # returns: none
    def submitStudent(self):
        # get student name from entry widget
        studentName = self.studentEntry.get().strip().title()
        #studentID = self.enterID.get().strip()
        student = self.studentRoster.findStudent(studentName)
        if student:
            messagebox.showerror("Error", "There is already a student with this name")
        else:
            message = self.studentRoster.addIndividualStudent(studentName)
            if message:
                messagebox.showinfo("Info", message)
            self.studentEntry.delete(0, END)
            self.studentRoster.saveData()


    # Function: fileUploadDisplay
    # enter a text file name display
    # parameters: none
    # returns: none
    def fileUploadDisplay(self):
        self.clearRows()
        self.fileNameLbl.grid(row = 11, column = 0, sticky='w')
        self.enterFileName.grid(row = 11, column = 1, sticky='w')
        self.submitFileBtn.grid(row = 11, column = 2, sticky = 'w')


    # Function: uploadFile
    # get file name and pass it to uploadStudentFile in the Roster module
    # parameters: none
    # returns: none
    def uploadFile(self):
        fileName = self.enterFileName.get().strip()  # get file name from entry widget
        message = self.studentRoster.uploadStudentFile(fileName)
        messagebox.showinfo("Info", message)
        self.enterFileName.delete(0, END)
        self.studentRoster.saveData()
    

    # Function: addCourseDisplay
    # displays required fields for adding a course
    # parameters: none
    # return: none
    def addCourseDisplay(self):
        self.clearRows()
        self.gridStudentWidgets()
        self.courseEntry.delete(0, END)
        self.gradeEntry.delete(0, END)
        self.commentBox.delete(0.0, END)
        self.dropDown.set("Select a semester") # Set default text
        self.courseLbl.grid(row = 10, column = 0, sticky = 'w')
        self.courseEntry.grid(row= 10, column = 1, sticky = 'w')
        self.semesterLbl.grid(row= 11, column= 0, sticky= 'w')
        self.dropDown.grid(row= 11, column= 1, sticky= 'w')
        self.gradeLbl.grid(row= 12, column= 0, sticky= 'w', padx= 2, pady= 2)
        self.gradeEntry.grid(row= 12, column = 1, sticky= 'w', padx= 2, pady= 2)
        self.commentLbl.grid(row= 13, column= 0, sticky= 'w')
        self.commentBox.grid(row= 13, column= 1, sticky= 'w')
        self.submitGradeBtn.grid(row= 14, column= 1, sticky= 'w')


    # Function: submitGrade
    # checks input and calls addCourseGrade in Student module when appropriate
    # parameters: none
    # returns: none
    def submitGrade(self):
        studentName = self.studentEntry.get().title().strip()
        courseName = self.courseEntry.get().upper().strip()
        semester = self.chosenSemester.get()
        courseGrade = self.gradeEntry.get().upper().strip()
        comment = self.commentBox.get(1.0, END).strip()
        message = "" 

        if not studentName or not courseName:
            message = "Student and Course names are required."
        elif semester == "Select a semester":
            message = "Please select a semester"
        else:
            # check if there is a student object with this name
            student = self.studentRoster.findStudent(studentName)
            if student:
                course = student.addCourseGrade(courseName, semester, courseGrade)
                self.studentRoster.saveData()
                if course:
                    self.studentEntry.delete(0, END)
                    self.courseEntry.delete(0, END)
                    self.chosenSemester.set("Select a semester")
                    self.gradeEntry.delete(0, END)
                    self.commentBox.delete(0.0, END)
                    if comment:
                        course.comment = comment
                else:
                    message = student.studentName + " is already enrolled in this course"
            else:
                message = studentName + " is not in your roster."
        if message: 
            messagebox.showinfo("Message", message)


    # Function: listStudentsDisplay
    # Displays a text widget and calls listStudents in the Roster module
    # Parameter: none
    # Returns: none
    def listStudentsDisplay(self):
        self.clearRows()
        self.listStudentsText.delete(0.0, END)
        self.listStudentsText.grid(row = 9, column = 0, sticky = 'w')

        message = ('\n'.join(self.studentRoster.listStudents()))
        self.listStudentsText.insert(1.0, message)


    # Funtion: lookUpDisplay
    # display elements to allow user to look up a student's grade in a course
    # Parameters: none
    # returns: none
    def lookUpDisplay(self):
        self.clearRows()
        self.gridStudentWidgets()
        self.courseEntry.delete(0, END)
        self.courseLbl.grid(row = 10, column = 0, sticky = 'w')
        self.courseEntry.grid(row= 10, column = 1, sticky = 'w')
        self.submitCourseBtn.grid(row= 10, column= 2, sticky= 'w')


    # Function: lookUpInfo
    # validates input and calls lookUpGrade in Student roster
    # Parameters: none
    # return: none
    def lookUpInfo(self):
        studentName = self.studentEntry.get().title().strip()
        courseName = self.courseEntry.get().upper().strip()
        if not studentName or not courseName:
            messagebox.showerror("Error", "Student and Course are required fields.")
        else:
            # check if there is a student with this name
            student = self.studentRoster.findStudent(studentName)
            if student:
                course = student.enrolledStatus(courseName)
                if course:
                    message = student.studentName + "'s grade in "
                    message += courseName + " (" + course.semester + "): " + course.courseGrade
                else: 
                    message = studentName + " does not take this course"
                messagebox.showinfo("Info", message)
            else:
                # ask user if they want to add student who is not in their roster
                answer = messagebox.askyesno("Add student?", "This student is not in your roster. Do you wnat to add " + studentName + "?")
                if answer:
                    result = self.studentRoster.addIndividualStudent(studentName)
                    messagebox.showinfo("Message", result)
    

    # Function: 
    #
    # Parameters: None
    # Returns: None
    def addCommentDisplay(self):
        self.clearRows()
        self.courseEntry.delete(0, END)
        self.commentBox.delete(1.0, END)
        self.gridStudentWidgets()
        self.courseLbl.grid(row = 10, column = 0, sticky = 'w')
        self.courseEntry.grid(row= 10, column = 1, sticky = 'w')
        self.commentLbl.grid(row= 11, column= 0, sticky= 'w')
        self.commentBox.grid(row= 11, column= 1, sticky= 'w')
        self.submitCommentBtn.grid(row= 12, column= 0, sticky= 'w')
        

    # Function: 
    #
    # Parameters: None
    # Returns: None
    def addCommentInfo(self):
        studentName = self.studentEntry.get().title().strip()
        courseName = self.courseEntry.get().upper().strip()
        comment = self.commentBox.get(1.0, END).strip()
        if comment:
            message = ""
            if not studentName or not courseName:
                messagebox.showerror("Error", "Student and Course are required fields.")
            else:
                # check if there is a student with this name
                student = self.studentRoster.findStudent(studentName)
                if student: 
                    # check if student takes this course
                    course = student.enrolledStatus(courseName)
                    if course: 
                        if course.comment:
                            answer = messagebox.askyesno("Add comment?", studentName + " has a comment in this course already. Do you want to replace it?")
                            if answer:
                                message = course.setComment(comment)
                        else:
                            message = course.setComment(comment)
                else: 
                    message = studentName + " does not take this course"
                self.commentBox.delete(1.0, END)
                self.commentBox.insert(1.0, message)


    # Function: 
    #
    # Parameters: None
    # Returns: None
    def saveReportCardDisplay(self):
        self.clearRows()
        self.gridStudentWidgets()
        self.semesterLbl.grid(row= 10, column= 0, sticky= 'w')
        self.dropDown.grid(row= 10, column= 1, sticky= 'w')
        self.saveReportCardBtn.grid(row= 10, column= 2, sticky= 'w')


    # Function: 
    #
    # Parameters: None
    # Returns: None
    def saveReportCard(self):
        studentName = self.studentEntry.get().strip().title()
        semester = self.chosenSemester.get()
        student = self.studentRoster.findStudent(studentName)
        if student:
            fileName = studentName + "_" + semester + ".txt"
            fileName = fileName.replace(" ", "")
            try:
                with open(fileName, "w") as file:
                    file.writelines(student.generateReportCard(semester))
                    messagebox.showinfo("Success", "File saved as " + fileName)
            except:
                messagebox.showerror("Error", "Could not save file")
        else:
            messagebox.showerror("Error", "Student not found")


    # Function: 
    #
    # Parameters: None
    # Returns: None
    def saveTranscriptDisplay(self):
        self.clearRows()
        self.gridStudentWidgets()
        self.saveTranscriptBtn.grid(row= 9, column= 2, sticky= 'w')


    def saveTranscript(self):
        studentName = self.studentEntry.get().strip().title()
        student = self.studentRoster.findStudent(studentName)
        student = self.studentRoster.findStudent(studentName)
        if student:
            fileName = studentName + "_Transcript.txt"
            fileName = fileName.replace(" ", "")
            try:
                with open(fileName, "w") as file:
                    file.writelines(student.generateTranscript())
                    messagebox.showinfo("Success", "File saved as " + fileName)
            except:
                messagebox.showerror("Error", "Could not save file")
        else:
            messagebox.showerror("Error", "Student not found")


    def gridStudentWidgets(self):
        self.studentEntry.delete(0, END)
        self.studentLbl.grid(row = 9, column = 0, sticky = 'w')
        self.studentEntry.grid(row = 9, column = 1, sticky = 'w')
    

    # Function: exitProgram
    # save and exit 
    # Parameters: none
    # return: none
    def exitProgram(self):
        self.studentRoster.saveData()
        self.master.destroy()


if __name__ == "__main__":
    print("This is a module and is meant to be imported")