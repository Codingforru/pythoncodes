# cocept of polymorphism
"""can be done in 4 ways:  1. duck typing    2.operator overloading
                            3.method overloading   4.method over riding"""
#1.duck typing

class pycharm:
    def execute(self):
        print('compling')
        print('running')

class myeditor:
    def execute(self):
        print('spell check')
        print('conventioning')
        print('compling')
        print('running')



class laptop:                       #1. for running the method code we need to we need to define the object for laptop
    def code(self,ide):
        ide.execute()


ide=myeditor()            #4. we create the object for ide, and type of ide is not fixed it can be pycharm or myeditor
                          #5. provided both the class should have method execute in it.(we can use either of them)
lap1=laptop()            #2. created
lap1.code(ide)            # 3. with help of the lap1 we can call code
                           # in code we need to pass the argument ide