#2. operator overloading    #

class student:                        #2. in our class there is no such add method , complier is getting error
    def __init__(self,m1,m2):
        self.m1=m1
        self.m2=m2
                                       #this is called operator overloading
    def __add__(self,other):             #3. here we define the add method ,it can be our choice to define whatever way
        m1=self.m1+ other.m1
        m2=self.m2+other.m2
        s3=student(m1,m2)
        return s3

    def __gt__(self,other):
        r1=self.m1+self.m2
        r2= other.m1+other.m2
        if r1>r2:
            return True
        else:
            return False
    def __str__(self):
        return '{} {}'.format(self.m1,self.m2)

s1= student(68,56)
s2=student(23,89)

s3= s1+s2
print(s3.m1)
if s1>s2:
    print('s1 wins')
else:
    print('s2 wins')


a=6
b=9
print(a+b)
print(int.__add__(a,b)) #1. at the background this is happenning , means there is the class of int where add is a method

print(a)
print(a.__str__())               # at the background this is happenning
print(s1.__str__())             # why not this is printing the value, why the adress
print(s2)                       # so we need to overload the str method here
print(s1)
