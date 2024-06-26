class Person:
    #assigning attributes
    def __init__(self, name, age, cid):
        self.name = name
        self.age = age
        self.cid = cid

    #defining behaviours/ methods
    def walk(self):
        print(self.name, "is walking")

    def Talk(self):
        print(self.name, "is talking")

    def sleep(self):
        print(self.name, "is sleeping")

    def eat(self):
        print(self.name, "is eating")

class Teacher(Person):
    def __init__(self, name, age, cid, subject, salary, department, designation):
        super().__init__(name, age, cid)
        self.subject = subject
        self.salary = salary
        self.department = department
        self.designation = designation

    def teach(self):
        print(self.name, "is teaching")

    def grade_students(self):
        print(self.name, "is grading")

    def attend_meeting(self):
        print(self.name, "is attending meeting")

class Student(Person):
    def __init__ (self,  name, age, cid, student_id, course, year, GPA):
        super().__init__(name, age, cid)
        self.student_id = student_id
        self.course = course
        self.year = year
        self.GPA = GPA

    #behaviours
    def study(self):
        print(self.name, "is studying")

    def attend_class(self):
        print(self.name, "is attending class")

    def write_exam(self):
        print(self.name, "is writing exam")

t1 = Teacher("Yashi", 30, 12345, "accounts", 30000, "commerce", "assistant")
t2 = Teacher("Dorji", 31, 67891, "physics", 20000, "commerce", "Ful teacher")


s1 = Student("penjor", 18, 1111, 12345, "bbi", 1, 3)
s2 = Student("lala", 19, 2222, 34561, "bbi", 1, 3.2)

#if s1.GPA > s2.GPA:
#    print(s1.name, "is better than", s2.name)
#    student_information = "year: " + str(s1.year) + "course: " + s1.course
#    print(student_information)
#else:
#    print(s2.name, "is better than", s1.name)
 #   student_information = "year: " + str(s1.year) + "course: " + s1.course
 #   print(student_information)

student_storage = [s1, s2]
 
for std in student_storage:
    print(std.name)
    print(std.GPA)
    print(std.year)
    print(std.course)
    