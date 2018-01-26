#Filename: training_set.py

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

#edge features
def edge_linked(m, n):
    if G.has_edge(m, n):
        return "positive"
    else:
        return "negative"

def common_friends(m, n):
    return len(list(set(G.neighbors(m)).intersection(set(G.neighbors(n)))))

def total_friends(m, n):
    return len(list(set(G.neighbors(m)).union(set(G.neighbors(n)))))

def jaccard_coefficient(m, n):
    return float(common_friends(m, n))/total_friends(m, n)

def preferental_attachment_score(m, n):
    return len(G.neighbors(m))*len(G.neighbors(n))

def friends_measure(m, n):
    count = 0
    
    for x in G.neighbors(m):
        for y in G.neighbors(n):
            if (x == y or G.has_edge(x, y)):
                count = count + 1
    return count

#edge subgraph features

def nh_subgraph(m, n):
    return G.subgraph(list(set(G.neighbors(m)).union(set(G.neighbors(n))))).number_of_edges()

def inner_subgraph(m, n):
    count = 0
    
    for x in G.neighbors(m):
        for y in G.neighbors(n):
            if G.has_edge(x, y):
                count = count + 1
    return count

def scc_nh_subgraph(m, n):
    return nx.number_connected_components(G.subgraph(list(set(G.neighbors(m)).union(set(G.neighbors(n))))))

#path features

def shortest_path(m, n):
    return nx.shortest_path_length(G, m, n)
  
#training set
f =file('training_set.csv','w')
writer = csv.writer(f)
writer.writerow(['node_out', 'node_in',
                 'edge_linked(m, n)', 'common_friends(m, n)',
                 'total_friends(m, n)', 'jaccard_coefficient(m, n)',
                 'preferental_attachment_score(m, n)', 'friends_measure(m, n)',
                 'nh_subgraph(m, n)', 'inner_subgraph(m, n)', 'scc_nh_subgraph(m, n)'
                 ])

count_number = 0
while count_number < 1000:
    count_number = count_number +1
    
    if(count_number > 0 and count_number % 100 == 0):
        print count_number
        
    edge = random.choice(G.edges())
    m = edge[0]
    n = edge[1]


    data = [m, n, 
            edge_linked(m, n), common_friends(m, n),
            total_friends(m, n), jaccard_coefficient(m, n),
            preferental_attachment_score(m, n), friends_measure(m, n),
            nh_subgraph(m, n), inner_subgraph(m, n), scc_nh_subgraph(m, n)
            ]
    writer.writerow(data)
    
        

count_number = 0

while count_number < 1000:
    
    if(count_number > 0 and count_number % 100 == 0):
        print count_number
        
    edge = random.sample(G.nodes(), 2)
    m = edge[0]
    n = edge[1]

    if edge_linked(m, n) == "negative" :
       
       data = [m, n,
               edge_linked(m, n), common_friends(m, n),
               total_friends(m, n), jaccard_coefficient(m, n),
               preferental_attachment_score(m, n), friends_measure(m, n),
               nh_subgraph(m, n), inner_subgraph(m, n), scc_nh_subgraph(m, n)
              ]
       writer.writerow(data)

       count_number = count_number +1
       
f.close()    
                


    
