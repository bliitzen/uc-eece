# HW 2p1 Task2
# File: HW_2p1_Team259_franceci.py
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
#This program allows the user to read in a text file containing initial velocity and different launch angle.
# The program then uses this data and calculates max height, time impact, and distance traveled.
# The program then rewrites the new data into a new .txt file called "results.txt".

def projY(t, V, A):
    return(-(9.81 *t**2)/2)+V*math.sin(A)*t

import math
fid = open("projectile.txt.", "r")
init_V = []
launchAng = []
count = 0
g = 9.81

for i in fid:
    init_V.append(int(i[0:2]))
    launchAng.append(int(i[3:]))
    count = count + 1
    
fid.close()

res = open('results.txt', 'w+')
timp = 0
tmax = 0
xdist = 0
for i in range(count):
    radians=launchAng[i]*(math.pi/180)
    timp = (2 * init_V[i] * math.sin(radians)) / g
    tmax = (init_V[i] * math.sin(radians)) / g
    xdist = (init_V[i] * math.cos(radians) * timp)

    res.write('{0:.2f} \t {1:.2f}\t {2:.2f}\t {3:.2f}\t {4:.2f}\n'.format(init_V[i],launchAng[i],timp,projY(tmax, init_V[i], launchAng[i]),xdist))

res.close()
             


