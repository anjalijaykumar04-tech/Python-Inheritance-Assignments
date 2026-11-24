class Employee:
    def salary(self):
        print("Employee salary: 25000")

class Manager(Employee):
    def salary(self):
        print("Manager salary: 60000")

e = Employee()
e.salary()

m = Manager()
m.salary()