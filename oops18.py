#3. method overloading  (doesnt support directly in python)
""" can we have 2 method  of same name in a class in which 1 take the
 2argument and other can take 3 argument """

class student:
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
    def sum(self,a=None,b=None,c=None):       #2. to work with 3 arguments we can proceed as a=none
        if a!=None and b!=None and c!=None:
            s = a+b+c
        elif a!=None and b!=None:
            s= a+b
        else:
            s=a

        return s

s1=student(56,58)
print(s1.sum(6,9))             #1. so this works
print(s1.sum(6,8))     # what if we pass 2 arguments -error


