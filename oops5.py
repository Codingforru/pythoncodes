#
class computer:
    def __init__(self):
        self.name= 'navin'
        self.age = 28
#
    def update(self):
        self.age= 28
    def compare(self,other):
        if self.age==other.age:
            return True
        else:
            return False


c1 = computer()
c2 = computer()
# so how can we compare between c1 and c2.
print(c1.name)
print(c2.name)
c1.update()
# here c1 is self and other as c2
if c1.compare(c2):
    print("they are same")
else:
    print('they are different')


