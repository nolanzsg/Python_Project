#Filename: time_distribution.py

import csv
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw
from scipy import special
from scipy import stats
import mpmath
import numpy as np


#generate data from the file

file = open('C:\users\zhusuoge\desktop\data.csv')
file.readline()
reader = csv.reader(file)
time_list = []
count_number = 0

#time distribution

for row in reader:
    count_number = count_number +1

    if(count_number % 10000 == 0):
        print count_number

    if (row[6] and (row[0] and row[7])):
        if int(row[6]) > 0:
            time_list.append(int(row[6]))
        
print max(time_list)

plt.figure(1)

p, t2 = np.histogram(time_list, bins=500,density = True)
t2 = (t2[:-1] + t2[1:])/2
plt.loglog(t2, p, "-o")

#plt.hist(time_list,2000,range =(0,2000), normed = True)

##results = powerlaw.Fit(time_list)
##results.plot_pdf(color = 'black', linestyle = '--')


plt.savefig("time_distribution.png")
##
##plt.figure(1)
##

##plt.savefig("time_distribution.png")

