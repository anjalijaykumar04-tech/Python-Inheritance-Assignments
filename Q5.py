class Father:
    def father_name(self):
        print("Father: Rajesh")

class Mother:
    def mother_name(self):
        print("Mother: Priya")

class Child(Father, Mother):
    def child_name(self):
        print("Child: Rahul")

c = Child()
c.father_name()
c.mother_name()
c.child_name()