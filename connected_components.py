#Filename: connected_components.py

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
components_nodes_list = []
components_edges_list = []

#create a graph

G = nx.Graph()
count_number = 0
for row in reader:
    count_number = count_number +1
    
    if(count_number % 100000 == 0):
        print count_number
        
    if (row[0] and row[7] and (int(row[6])>0)):

        if   row[4] == "01":
            G.add_edge(row[0], row[7])
        elif row[4] == "02":
            G.add_edge(row[7], row[0])
print "number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                         G.number_of_edges())
#connected components

H = nx.connected_component_subgraphs(G)

for i in range(1, len(H)):
    components_nodes_list.append(H[i].number_of_nodes())
    components_edges_list.append(H[i].number_of_edges())

plt.figure(1)

p, t2 = np.histogram(components_nodes_list, bins=500,density = True)
t2 = (t2[:-1] + t2[1:])/2
plt.loglog(t2, p, "-o", linewidth = 2)

plt.savefig("components_nodes_distribution.png")


plt.figure(2)

p, t2 = np.histogram(components_edges_list, bins=500,density = True)
t2 = (t2[:-1] + t2[1:])/2
plt.loglog(t2, p, "-o", linewidth = 2)

plt.savefig("components_edges_distribution.png")

