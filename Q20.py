class School:
    def school_name(self):
        print("School: ABC School")

class Student(School):
    def student_name(self):
        print("Student: Rahul")

class Exam(Student):
    def percentage(self, marks, total):
        print("Percentage:", marks / total * 100)

e = Exam()
e.school_name()
e.student_name()
e.percentage(450, 500)