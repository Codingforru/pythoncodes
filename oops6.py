# types of variable in oops; 1. class(static ) variable   2. instance variable
#class variable is defined outside the init. and is fixed
# instance(object) variable is written inside init
class car:
    # class varible
    wheels=5
    def __init__(self):
        #instance variable
        self.mil=10
        self.comp= 'bmw'

c1= car()
c2= car()
# name space: area where u create and store object/variable
# class name space   instance name space
# here if we change the class variable it will be share for both object
car.wheels=8
print(c1.comp,c1.mil,c1.wheels)
print(c2.comp, c2.mil,c2.wheels)
