#Filename: weighted_set.py

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

data = open('C:\users\zhusuoge\desktop\call.csv')
#data.readline()
reader = csv.reader(data)

#create a graph

G = nx.Graph()
count_number = 0
for row in reader:
    count_number = count_number +1
    
    if(count_number % 100000 == 0):
        print count_number
    if count_number > 1:
        
        if (row[0] and row[7] and (int(row[6])>0)):
            if G.has_edge(row[0],row[7]):
                
                total_length = int(row[6])+int(G[row[0]][row[7]]["length"])
                total_times = 1 + int(G[row[0]][row[7]]["times"])
            else:
                total_length = int(row[6])
                total_times = 1
                
            G.add_edge(row[7], row[0],length =total_length, times =total_times)
            
print "number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())

G = nx.strongly_connected_component_subgraphs(G)[0]

print "number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())
for a in G.edges():
    m = a[0]
    n = a[1]

    if int(G[m][n]["times"]) < 20:
        G.remove_edge(m, n)
    

print "removed those times < 20,number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())
G = nx.strongly_connected_component_subgraphs(G)[0]

print "removed those times < 20 and strong_connected_component number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())
#times

time_list = []
for a in G.edges():
    m = a[0]
    n = a[1]
    time_list.append(int(G[m][n]["times"]))

dmax = max(time_list) + 1

freq =[0 for d in range(dmax)]
for d in time_list:
	
    freq[d] += 1
    
plt.figure(1)

x = range(len(freq))
y = [z for z in freq]
plt.loglog(x, y, color = 'red', marker = "o", linewidth = 2)
plt.savefig("times_distribution.png")

#length

length_list = []

for a in G.edges():
    m = a[0]
    n = a[1]
    length_list.append(int(G[m][n]["length"]))

dmax = max(length_list) + 1

freq =[0 for d in range(dmax)]
for d in length_list:
	
    freq[d] += 1
    
plt.figure(2)

x = range(len(freq))
y = [z for z in freq]
plt.loglog(x, y, color = 'red', marker = "o", linewidth = 2)
plt.savefig("length_distribution.png")

