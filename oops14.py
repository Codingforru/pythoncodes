

                                # {constructor in inheritence}
class A:                         # A is the constructor (SUPER CLASS)
    def __init__(self):               #1 init constructor automatically gets called
        print("in A init")
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):                                        #2 B is subclass of A
    def __init__(self):                           #4 WHAT IF B has its own init constructer
        super().__init__()                         #7 WHAT IF want to print the init of A also
                                                  #8 we use special keyword super().
        print("in B init")
    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")


a1=B()                               # 3even if we call B , INIT of A gets called
                                      # 5 now it will print init of B.
                                      # 6 first it will check in b for init then go to A

