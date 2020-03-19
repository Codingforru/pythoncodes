# types of methods:
#1. instance method  2. class method  3. static method
class student:
    #defining the class variable
    school='dav'

    def __init__(self, m1,m2,m3):
        self.m1= m1
        self.m2=m2
        self.m3=m3
    def avg(self):
        return ( self.m1+ self.m2+ self.m3)/3
    # get methods
    def get_m1(self):
        return self.m1
    def set_m1(self,value):
        self.m1=value
        return self.m1


 # passing the arguments m1,m2,m3 (instance variable)

s1= student(60,40,52)
s2= student(85,46,63)
# avg here is the instance method( because it works with object).
#instance method has itself of two types. 1.accessor  2.mutators

#1.accesors- if we only wants fetching the value of instance variable (get method)
#2.mutators- if we want to modify the values we use mutators(set method)

print(s1.avg())
print(s2.avg())
print(s1.get_m1())
print(s1.set_m1(69))







