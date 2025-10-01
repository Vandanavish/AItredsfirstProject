#Q1: Write a python program to add all the odd numbers from 0 to 20.
sum_of_odd=0
for i in range(21):
    if i%2 !=0:
       sum_of_odd += i

print("Sum of odd number from 0 to 20 :",sum_of_odd)