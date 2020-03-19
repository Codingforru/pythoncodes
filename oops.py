# object oriented programming
# in this we have class and object
#class-design (blueprint)
#object is the isinstance()

# defining the class

class computer:
    def config(self):
        print('i5, 16gb,1tb')

# defing the object
comp1= computer()
# knowing the class of comp1
print(type(comp1))
# now how to call the method(function)
computer.config(comp1)
#other method used generally
comp1.config()
