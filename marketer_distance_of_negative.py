#Filename: marketer_distance_of_negative.py

import csv
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw
from scipy import special
from scipy import stats
import mpmath
import numpy as np
import random
import math
#generate data from the file

data = open('C:\users\zhusuoge\desktop\TheMarkerAnonymized.csv')
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
        if (row[0] and row[1]):
            G.add_edge(row[0], row[1])
        
print "number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())

data.close()

#remove the isolated edges

##for isolated_edges in G.edges():
##    if (G.degree(isolated_edges[0])==1 and G.degree(isolated_edges[1])==1):
##        G.remove_nodes_from([isolated_edges[0],isolated_edges[1]])
##        
##print "updating number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
##                                                        G.number_of_edges())
#strong connected components subgraph
G = nx.strongly_connected_component_subgraphs(G)[0]

print "strong_connected components number of nodes is %d \nnumber of edges is %d" %(G.number_of_nodes(),
                                                        G.number_of_edges())



#edge features
def edge_existed(m, n):
    
    if G.has_edge(m, n):
        return 1
    else:
        return 0

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
    
    return (len(G.neighbors(m)))*(len(G.neighbors(n)))
    

def neighbors_affinity(m, n):
    count = 0
    
    
    for x in G.neighbors(m):
        for y in G.neighbors(n):
            if G.has_edge(x, y):
                count = count + 1
    return float(count)/float((math.log10(len(G.neighbors(m))+1))*(math.log10(len(G.neighbors(n))+1)))
    

#edge subgraph features

##def nh_subgraph(m, n):
##    return G.subgraph(list(set(G.neighbors(m)).union(set(G.neighbors(n))))).number_of_edges()- edge_existed(m, n)
##
##def inner_subgraph(m, n):
##    count = 0
##    
##    for x in G.neighbors(m):
##        for y in G.neighbors(n):
##            if G.has_edge(x, y):
##                count = count + 1
##    return count - edge_existed(m, n)
##                                                    
##def scc_nh_subgraph(m, n):
##    return nx.number_connected_components(G.subgraph(list(set(G.neighbors(m)).union(set(G.neighbors(n))))))

#path features

def shortest_path(m, n):
    
    return nx.shortest_path_length(G, m, n)
    
  
#training set
f =file('marker_distance of negative_.csv','w')
writer = csv.writer(f)
writer.writerow(['node_out', 'node_in',
                 'edge_linked(m, n)', 'common_friends(m, n)',
                 'total_friends(m, n)', 'jaccard_coefficient(m, n)',
                 'preferental_attachment_score(m, n)', 'neighbors_affinity(m, n)','shortest_path_length(m,n)'
                 ])

##count_number = 0
##while count_number < 10000:
##    count_number = count_number +1
##    
##    if(count_number > 0 and count_number % 100 == 0):
##        print count_number
##        
##    edge = random.choice(G.edges())
##    m = edge[0]
##    n = edge[1]
##
##    G.remove_edge(m,n)
##
##
##    data = [m, n, 
##            edge_linked(m, n), common_friends(m, n),
##            total_friends(m, n), jaccard_coefficient(m, n),
##            preferental_attachment_score(m, n), neighbors_affinity(m, n),shortest_path(m, n)
##            ]
##    G.add_edge(m,n)
##    
##    writer.writerow(data)
##    
##        

count_number = 0

while count_number < 10000:
    
    if(count_number > 0 and count_number % 100 == 0):
        print count_number
        
    edge = random.sample(G.nodes(), 2)
    m = edge[0]
    n = edge[1]

    if edge_linked(m, n) == "negative" :
       
       data = [m, n,
               edge_linked(m, n), common_friends(m, n),
               total_friends(m, n), jaccard_coefficient(m, n),
               preferental_attachment_score(m, n), neighbors_affinity(m, n),shortest_path(m, n)
               ]
       writer.writerow(data)

       count_number = count_number +1
       
f.close()    
                


    
