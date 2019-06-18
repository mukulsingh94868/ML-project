#!/usr/bin/python3

import matplotlib.pyplot as plt
#  only loading python ori lib

x=[2,3]
x1=[4,3,8]
y=[9,5]
y1=[2,9,7]


plt.xlabel("time")
plt.ylabel("speed")
plt.plot(x,y,label="water")  # thus will draw a straight line
plt.plot(x1,y1,label="sand")  # thuis will draw a straight line
plt.grid(color='green')  #  to form grid in graph
plt.legend() #  # to show labels with plot
plt.xlim(0,12)  #  to show min and max number in x axis
plt.ylim(0,15)   #  y axis
plt.show
