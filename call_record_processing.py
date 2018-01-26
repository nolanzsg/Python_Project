#Filename: call_record_processing.py

import csv
import networkx as nx
import matplotlib.pyplot as plt
import powerlaw
from scipy import special
import mpmath

#generate data from the file

file = open('C:\users\zhusuoge\desktop\data.csv')
file.readline()
reader = csv.reader(file)

#create a graph

G = nx.DiGraph()
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
           
#####degree distribution
    
degree = nx.degree_histogram(G)
#print nx.degree_histogram(G)

plt.figure(1)

x = range(len(degree))
y = [z / float(sum(degree)) for z in degree]
plt.loglog(x, y, color = 'red', marker = "o", linewidth = 2)

data_degree = list(G.degree().values())

#fixed xmin
results = powerlaw.Fit(data_degree, discrete = True, xmin = 1.0)
results.plot_pdf(color = 'blue', marker = "v", linewidth = 2)

#estimating xmin
results = powerlaw.Fit(data_degree, discrete = True)
results.plot_pdf(color = 'green', marker = "D", linewidth = 2)
results.power_law.plot_pdf(color = 'black', linestyle = '--')
plt.savefig("degree_distribution.png")

R, p = results.distribution_compare('power_law', 'exponential', normalized_ratio=True)
print "power_law and exponential", R, p
R, p = results.distribution_compare('power_law', 'truncated_power_law', normalized_ratio=True)
print "power_law and truncated_power_law", R, p

print "best minimal value for power law fit of degree distribution: ", results.xmin
print "fixed xmin:", results.fixed_xmin
print "fitted value of alpha of degree distribution: ", results.power_law.alpha


#plt.show()

#####in_degree distribution

plt.figure(2)

degseq = list(G.in_degree().values())
dmax = max(degseq) + 1
freq = [0 for d in range(dmax)]

for d in degseq:
    freq[d] += 1

x = range(len(freq))
y = [z / float(sum(freq)) for z in freq]
plt.loglog(x, y, color = 'red', marker = "o", linewidth = 2)

#fixed xmin
results = powerlaw.Fit(degseq, discrete = True, xmin = 1.0)
results.plot_pdf(color = 'blue', marker = "v", linewidth = 2)

#estimating xmin
results = powerlaw.Fit(degseq, discrete = True)
results.plot_pdf(color = 'green', marker = "D", linewidth = 2)
results.power_law.plot_pdf(color = 'black', linestyle = '--')
plt.savefig("in_degree_distribution.png")

R, p = results.distribution_compare('power_law', 'exponential', normalized_ratio=True)
print "power_law and exponential", R, p
R, p = results.distribution_compare('power_law', 'truncated_power_law', normalized_ratio=True)
print "power_law and truncated_power_law", R, p

print "best minimal value for power law fit of in_degree distribution: ", results.xmin
print "fixed xmin:", results.fixed_xmin
print "fitted value of alpha of in_degree distribution: " , results.power_law.alpha


#####out_degree distribution

plt.figure(3)

degseq = list(G.out_degree().values())
dmax = max(degseq) + 1
freq = [0 for d in range(dmax)]

for d in degseq:
    freq[d] += 1

x = range(len(freq))
y = [z / float(sum(freq)) for z in freq]
plt.loglog(x, y, color = 'red', marker = "o", linewidth = 2)

#fixed xmin
results = powerlaw.Fit(degseq, discrete = True, xmin = 1.0)
results.plot_pdf(color = 'blue', marker = "v", linewidth = 2)

#estimating xmin
results = powerlaw.Fit(degseq, discrete = True)
results.plot_pdf(color = 'green', marker = "D", linewidth = 2)
results.power_law.plot_pdf(color = 'black', linestyle = '--')
plt.savefig("out_degree_distribution.png")

R, p = results.distribution_compare('power_law', 'exponential', normalized_ratio=True)
print "power_law and exponential", R, p
R, p = results.distribution_compare('power_law', 'truncated_power_law', normalized_ratio=True)
print "power_law and truncated_power_law", R, p

print "best minimal value for power law fit of out_degree distribution: ", results.xmin
print "fixed xmin:", results.fixed_xmin
print "fitted value of alpha of out_degree distribution: " , results.power_law.alpha




#clustering coefficient

#print "clustering_coefficient = %d" % nx.average_clustering(G)

#diameter and shortest path length

#diameter = nx.diameter(G)
#average_shortest_path_length = nx.average_shortest_path_length(G)

#assortativity

#degree_assortativity = nx.degree_assortativity(G)
