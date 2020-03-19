# iterators
num=[7,8,9,63,89,12,14]
# if we want to the values one by one  we can use for loop-1st method
for i in num:
    print(i)

#2. way would be define our iterator
it= iter(num)
print(it.__next__())   #next is the inbuilt function
print(it.__next__()) # at the second time it will print the next value
 # 2nd way of representing is print(next(it)) # so iterator preserves the privious value