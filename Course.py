# Course module
# creates Course class which manages course name and grade
# Shira Cheifetz 12/25/25

# Course class 
# creates course objects with course name and grade 
class Course(object):

    def __init__(self, name, semester, grade, comment= ""):
        self.__courseName = name.upper()
        self.semester = semester
        self.courseGrade = grade.upper() 
        self.comment = comment

    # print course information 
    def __str__(self):
        rep = "  Course: " + self.__courseName + ", Grade: " + self.courseGrade
        return rep
    
    # courseName property
    @property
    def courseName(self):
        return self.__courseName
    
    # courseName setter
    @courseName.setter
    def courseName(self, newCourseName):
        self.__courseName = newCourseName.upper()

    def setComment(self, comment):
        self.comment = comment
        return "Comment updated"


if (__name__ == "__main__"):
    print("This is a module and is meant to be imported")