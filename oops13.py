

                                                # {multiple inheritence}
class A:                                         # A is the constructor
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B():                                        # B is seperate class


    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")

class C(A,B):                                       # here if we write C as subclass of B and A

    def feature5(self):
        print("feature 5 is working")


a1=A()
b1=B()                               # but can not access features of A
c1=C()
a1.feature1()
a1.feature2()
b1.feature3()
c1.feature3()                       # HERE C will have acces to all features