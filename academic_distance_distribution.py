#Filename: academic_distance_distribution.py

import csv
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw
from scipy import special
from scipy import stats
import mpmath
import numpy as np
import random

#generate data from the file

data = open('C:\users\zhusuoge\desktop\Academia_distance of negative_.csv')
#data.readline()
reader = csv.reader(data)

distance_list = []

count_number = 0
for row in reader:
    count_number = count_number +1
    
    if count_number > 1:
        distance_list.append(int(row[8]))

dmax = max(distance_list) + 1

freq =[0 for d in range(dmax)]
for d in distance_list:
	
    freq[d] += 1
    
plt.figure(1)

x = range(len(freq))
y = [z for z in freq]
plt.plot(x, y, color = 'red', marker = "o", linewidth = 2)
plt.savefig("academic_distance_distribution.png")
