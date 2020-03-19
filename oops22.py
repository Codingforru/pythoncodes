# generators in python
# generator will give iterator
def topten():

   yield 1   # yield is the keyword which make our function as generator
   yield 2
   yield 3
   yield 4

values= topten()
print(next(values))  # if we want fetch something we use the next
print(next(values))
for i in values:    # it print the  remainning values
     print(i)

""" main difference between the return and yield is return will terminate the function
but yield will not"""