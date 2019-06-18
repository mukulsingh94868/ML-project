#!/usr/bin/python3

import matplotlib.pyplot as plt
#  only loading python ori lib

players=["virat","dhoni","pandaya"]
runs=[120,230,34]


plt.xlabel("players")
plt.ylabel("runs")
plt.bar(players,runs)
plt.grid(color='green')  #  to form grid in graph
plt.legend()   # to show labels with plot
plt.show
