#Filename: two_hops_count.py

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

data = open('C:\users\zhusuoge\desktop\data.csv')
#data.readline()
reader = csv.reader(data)

#create a graph

G = nx.Graph()
count_number = 0
for row in reader:
    count_number = count_number +1
    
    if(count_number % 100000 == 0):
        print count_number
        
    if (row[0] and row[7]):

        if   row[4] == "01":
            G.add_edge(row[0], row[7])
        elif row[4] == "02":
            G.add_edge(row[7], row[0])
print "number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())

data.close()

#strong connected components subgraph

G = nx.strongly_connected_component_subgraphs(G)[0]

print "number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())



def shortest_path(m, n):
    return nx.shortest_path_length(G, m, n)
  
        

count_number = 0

print "shortest path calculating completed"

for m in G.nodes():
    for n in G.nodes():
        if nx.shortest_path_length(G, source=m, target=n) == 2:
            count_number = count_number + 1
            if(count_number % 1000 == 0):
                print count_number/2
            

        
                


    
