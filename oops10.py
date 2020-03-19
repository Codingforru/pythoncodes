# lesson about inner class
class student:  # outer class
    def __init__(self, name, rollno):
        self.name = name
        self.rollno = rollno
        self.lap = self.laptop() # defining the object for inner class

    # 2nd way would be creating a laptop class inside the class

    def show(self):
        print(self.name, self.rollno)
        self.lap.show()

    class laptop:  # inner class
        def __init__(self):
            self.brand = 'hp'
            self.cpu = 'i5'
            self.ram = 8  # where to create the object of it? should in the outer class
        def show(self):
            print(self.brand,self.cpu,self.ram)


# if we want to add about laptop(cpu, ram), we can do it by 2ways
# 1st would simply add cpu and ram as 2 variable in init
s1 = student("abhay", 45)
s2 = student("sunil", 33)
# so if we want to print the both data of students
print(s1.name, s1.rollno)
# other way would be
s1.show()
# so we will call the inner class
print(s1.lap.brand)
# other way would be
# lap1 and lap2 are 2 diff object

lap1 = s1.lap              # we can create object of inner class inside the outer class
                         #or we create object of inner class outside the outer class provided you use outer class name to call
lap2 = s2.lap            # lap1= student.laptop()

print(id(lap1))
print(id(lap2))
