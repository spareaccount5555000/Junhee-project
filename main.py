class Student():
    register_num = 15
    name = "alex"
    studentsclass = 1
    level = 6
    grade = "A1"  

    def __init__(self):
        print("creating a new student")

    def changingdetails(self):
        self.grade = input("what is this student's new grade:")
        self.name = input("what is this student's new name:")
        self.level = input("what is this student's new level:")
    
    def displaydetails(self):
        print(self.register_num)
        print(self.name)
        print(self.studentsclass)
        print(self.level)
        print(self.grade)
    

ian = Student()
ian.changingdetails()
ian.displaydetails()
    





