                                # {METHOD RESOLUTION ORDER}
class A:                         # A is the constructor (SUPER CLASS)
    def __init__(self):               #1 init constructor automatically gets called
        print("in A init")
    def feature1(self):
        print("feature 1-a is working")
    def feature2(self):
        print("feature 2 is working")

class B:
    def __init__(self):
        print("in B init")
    def feature1(self):
        print("feature 1-b is working")
    def feature4(self):
        print("feature 4 is working")


class C(A,B):                                 #2. what if we want to print init of super class
                                             #3.which init will get printed?(AorB)
    def __init__(self):
        super().__init__()
        print("in C init")



a1=C()                            #1 IT will print the init of c
                                  #4.IT will print init of A
               #5.this is because of MRO(whenever there is multiple inheritance it will always start from left to write)

a1.feature1()                      #5. same thing happens with methods ,so it will print 1-a because of mro