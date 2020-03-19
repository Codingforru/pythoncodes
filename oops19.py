 # 4. method of over riding
class A:
    def show(self):
      print(' in a show')

class B(A):            # 2.if we make the b as the child class of a - it will work
    def show(self):
        print(' in b show')        #3.but if b has it own show then it will print that only
                                # 4. this is called method of overriding

a1=B()
a1.show()      # 1.this will not work as there is no such attribute in B
