# concept of inheritence  in oops
# class inherit a class                        #{ single level inheritence]
class A:                                         # A is the constructor
    def feature1(self):
        print("feature 1 is working")
    def feature2(self):
        print("feature 2 is working")

class B(A):                                   # here we write that b is the child class/ sub class of A. i.e B(A)
                                              # after doing this all the features of A Is available for B

    def feature3(self):
        print("feature 3 is working")
    def feature4(self):
        print("feature 4 is working")



a1=A()
b1=B()
a1.feature1()
a1.feature2()
b1.feature3()                               # here features of class is only available
                                             # if we what that features of A class should also be available
                                             # here comes picture of inheritance
