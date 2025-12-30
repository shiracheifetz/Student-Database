# Roster module
# creates Roster class which manages a dictionary of Student objects
# openFile, addStudents, addIndividualStudent, listStudents, and saveData functions
# Shira Cheifetz 12/25/25

import os 
import pickle
import Student

# Roster class
# creates Roster objects which manage a dictionary of Student objects
class Roster(object):
    def __init__(self, studentDict):
        self.studentDict = studentDict


    @staticmethod
    # Function: openFile
    # Purpose: try to open existing file with student data, if it doesn't exist create an empty dictionary
    # Parameters: none
    # Returns: none
    def openFile():
        # change directory to directory of current script            
        os.chdir(os.path.dirname(os.path.realpath(__file__)))

        try:
            fileSchool = open("school.dat", "rb") # open file in read binary mode
            studentDict = pickle.load(fileSchool) # load the data
            fileSchool.close()
        except:
            studentDict = {} # if the file doesn't exist yet, create an empty dictionary
        return studentDict


    # Function: addIndividualStudent
    # Purpose: Adds a single student to the roster
    # Parameter: str studentName
    # Returns: str message
    def addIndividualStudent(self, studentName):
        if not studentName:
            message = "Student name is required"
        elif not studentName.replace(" ", "").isalpha():
            message = studentName + " is not a valid student name"
        else:
            newStudent = Student.Student(self.studentDict, studentName)
            id = newStudent.id
            self.studentDict[id] = newStudent
            message = None
        return message


    # Function: uploadStudentFile
    # returns the contents of the file, if any
    # parameters: str fileName
    # returns: str message
    def uploadStudentFile(self, fileName):
        # find current directory
        currentDir = os.getcwd()
        contents = os.listdir(currentDir)

        duplicates = []  # keeps track of students who were already in the roster
        
        # check if the text file is in the same directory
        if fileName not in contents:
            message = fileName + " not found"

        else:
            filestudentNames = open(fileName, "r") # open file in read mode
            lines = filestudentNames.readlines() # reads the lines of the file into a list
            filestudentNames.close()
            if not lines:
                message = "The file is empty"
            else:
                message = "Added students from " + fileName
                # go through each line which is the name of each student
                for studentName in lines:
                    studentName = studentName.strip().title() 
                    for student in self.studentDict.values():
                        if student.studentName == studentName:
                            duplicates.append(studentName)
                            break
                    else:
                        self.addIndividualStudent(studentName) # add student
        if duplicates:
            message += " \nThe following were already in your roster: "
            message += ", ".join(duplicates)
        return message
                    

    # Function: findStudent
    # loops through the roster and finds any student with the specified name
    # Parameter: str studentName
    # returns: return student object or None
    def findStudent(self, studentName):
        for student in self.studentDict.values():
            if student.studentName == studentName:
                return student
        return None


    # Function: listStudents
    # Purpose: Lists existing students with their courses and grades, if applicable
    # Parameter: none
    # Returns: none
    def listStudents(self):
        # if studentDict is empty
        if not self.studentDict:
            messageList = ["There are no students yet in your roster"]
        else:
            messageList = ["All students along with their courses and corresponding grades: \n"]
            # go thru the dictionary, adding student info to the message list
            for id in self.studentDict:
                student = self.studentDict[id]
                messageList.append(student.studentName + " ID#" + student.id)
                if student.courseList:
                    for course in student.courseList:
                        messageList.append(course.courseName + " " + course.semesteer + ": " + course.courseGrade)
                messageList.append('\n')   
        return messageList
    

    # Function: saveData
    # Purpose: dump contents of studentDict into a data file
    # Parameter: none
    # Returns: none
    def saveData(self):
        fileSchool = open("school.dat", "wb") # open file in write binary mode
        pickle.dump(self.studentDict, fileSchool) # dump the updated list into the file
        fileSchool.close() # close file


if __name__ == "__main__":
    print("This is a module and is meant to be imported")