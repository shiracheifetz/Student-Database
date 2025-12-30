# Student module
# creates Student class which manages student name and list of Course objects
# printAllInfo, addCourseGrade, and lookUpGrade functions
# Shira Cheifetz 12/25/25

import Course 

# student class 
# creates student objects with name and list of courses
class Student(object):

    def __init__(self, studentDict, name):
        self.studentName = name.title()
        self.id = self.generateID(studentDict)
        self.__courseList = [] # list of Course objects
        self.transcriptSaves = 0

    # print student name
    def __str__(self):
        rep = "Name: " + self.studentName + '\n'
        return rep
    
    # *did not end up using this function*
    # # print all student information: name, courses, and grades
    # def printAllInfo(self):
    #     rep = "Name: " + self.studentName + '\n'
    #     for course in self.__courseList:
    #         rep += "  Course: " + course.courseName + ", Grade: " + course.courseGrade +'\n'
    #     return rep
    
    # courseList property
    @property
    def courseList(self):
        return self.__courseList
    
    # courseList setter
    @courseList.setter
    def courseList(self, courseList):
        self.__courseList = courseList


    def generateID(self, studentDict):
        if not studentDict:
            return "1001"
        
        # find the highest existing ID
        highestID = sorted(studentDict.keys(), key=int)[-1]
        # increment and return as string
        return str(int(highestID) + 1)


    # Function: addCourseGrade
    # Purpose: adds a course and grade for a student
    # Parameters: str courseName, str courseGrade
    # Returns: str message 
    def addCourseGrade(self, courseName, semester, courseGrade):
        # return to menu if course in already in student courseList
        for course in self.__courseList:
            if course.courseName == courseName:
                return None
        if courseGrade == "":
            courseGrade = "N/A" # set grade to N/A if user doesn't enter a grade

        # create course object and add to courseList
        courseObject = Course.Course(courseName, semester, courseGrade)
        self.__courseList.append(courseObject)
        # print the new information
        return courseObject
    

    # Function: lookUpGrade
    # Purpose: returns the student's grade in the course
    # Parameters: str courseName
    # Returns: str messsage
    def enrolledStatus(self, courseName):
        enrolledCourse = None  # return if student is not taking this course
        # print course and grade if found
        for course in self.__courseList:
            if course.courseName == courseName:
                enrolledCourse = course
        return enrolledCourse
    

    # call this on the studentRoster
    def getStudentID(self, studentName):
        for student in self.studentDict:
            if student.studentName == studentName:
                return student.id
        return None
    

    def generateReportCard(self, semester):
        lines = ["WITS Report Card for " + semester + "  |  " +  self.studentName + " ID#" + self.id +'\n'] # header
        lines.append("_" * 65 + "\n\n") # line for design
        for course in self.courseList:
            if course.semester == semester:
                lines.append(course.courseName + ": " + course.courseGrade + '\n')
                if course.comment:
                    lines.append("Comment: " + course.comment)
                lines.append('\n\n')
        return lines
    

    def generateTranscript(self):
        lines = ["WITS Transcript  |  " + self.studentName + " ID#" + self.id +'\n']
        lines.append("_" * 60 + "\n\n")
        for course in self.courseList:
            lines.append(course.courseName + " " + course.semester + ": " + course.courseGrade + '\n\n')
        return lines



if __name__ == "__main__":
    print("This is a module and is meant to be imported")