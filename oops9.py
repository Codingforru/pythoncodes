# 2. static method (not related to class variable or instance variable)

class student:
    school='dav'

    def __init__(self, m1,m2,m3):
        self.m1= m1
        self.m2=m2
        self.m3=m3
    # here we use decorators
    @classmethod
    def getschool(cls):
        return cls.school
    #if we need to perform some operation which has nothing to do with the class variable and instance variable
    #we go for satic method.
    @staticmethod
    def info():
        print('this is class 9')
s1= student(60,40,52)
s2= student(85,46,63)

#here we dont want to pass class (student)in info .so we need to use decorators

print(student.getschool())
student.info()


