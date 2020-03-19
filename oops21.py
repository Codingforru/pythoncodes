# what if we want to create our own iterator; for that we need two methods 1. iter  2. next

class topten:
    def __init__(self):
        self.num=1
    def __iter__(self):
        return self
    def __next__(self):   #3. if have provide the condition to stop
        if self.num<=10:
            val= self.num
            self.num+=1
            return val
        else:
            raise StopIteration

values= topten()
print(next(values))  #1. this works what is worng with for loop if we apply
                     # 2.we have to mention the end in the loop ,unless loop goes on continuing
for i in values:     # FOR 1. we have already got 1 as o/p, so the iterator will not print  the 1 again
    print(i)

