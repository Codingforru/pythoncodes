# size of the object is depends on the no. of variables and size of each varible
# who allocate the size to object?  - constructor (here computer() - is constructor)
class computer:
    def __init__(self):
        self.name= 'navin'
        self.age = 28
#again to understand the concept of self
    def update(self):
        self.name= 'rakhi'
        print(self.name)
        self.age= 29
        print(self.age)

c1 = computer()
c2 = computer()
#  this is way we can change the value of object
c1.name= 'abhay'
c1.age=26
print(c1.name,c1.age)
print(c2.name)

# other way 
# so here self will take which object as argument(c1 or c2)
# so it will automatically take same value of object which is called on.
c1.update()
print(c1.name)
print(c1.age)
