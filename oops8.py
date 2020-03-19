

# 2. class method(class variable used)

class student:
    school='dav'

    def __init__(self, m1,m2,m3):
        self.m1= m1
        self.m2=m2
        self.m3=m3
    # here we use decorators
    @classmethod
    def info(cls):
        return cls.school

s1= student(60,40,52)
s2= student(85,46,63)

#here we dont want to pass class (student)in info .so we need to use decorators

print(student.info())



