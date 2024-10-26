### Part Four -- your code goes here. 
import random

list = []
for i in range(10):
    list.append(random.randint(1,100))
odd =[]
while i< 10:
    for i in list:
        if i % 2 == 0:
            list.pop(0)
            continue 
        else:
            odd.append(i)
print(odd)
