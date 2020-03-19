# special variable (attributes),methods

class computer:
    # init method is automatically called ,they dont need to call
    def __init__(self,cpu,ram):
       self.cpu=cpu
       self.ram=ram

# we cant pass simply cpu or ram , we need to specify the  object on which they belong (self)
    def config(self):
        print('config is',self.cpu,self.ram)
#the 3rd rgument is already there as object (cpmp1)
comp1= computer('i5',16)
comp2= computer('ryzen3',8)

#other method used generally
comp1.config()
comp2.config()

