# HW 2p1 Task1
# File: HW_2p1_Task1_Team259_franceci.py
# Date:    30 January 2020
# By:      Christian France
# Section: 019
# Team:    259
# 
# ELECTRONIC SIGNATURE
# Christian France
#
# The electronic signature above indicates the script
# submitted for evaluation is my individual work, and I
# have a general understanding of all aspects of its
# development and execution.
#
#This program allows the user to enter a number for how many perrin sequence numbers they
# want to calculate.

n = int(input("Enter a positive integer n: "))

while (n < 0):
    n = int(input("Please enter a POSITIVE INTEGER n: "))

myList = [3, 0 , 2, 3, 2, 5]

if(n < 6):
    print(myList[0:n])
    
else:
    for i in range(6, n):
        k = myList[i-2] + myList[i-3]
        myList.append(k)
    print(myList)

