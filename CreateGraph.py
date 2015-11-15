import networkx as nx
import sys
import os
import operator
import numpy as np
from scipy import stats
import collections
import matplotlib
try:
    import matplotlib.pyplot as plt
except:
    raise
#46.971km, 47.271km
#47.149km, 
#North Latitude: 40.915256 South Latitude: 40.491370 East Longitude: -73.700272 West Longitude: -74.259090
#See more at: http://www.mapdevelopers.com/geocode_bounding_box.php#sthash.A66HooOI.dpuf
G=nx.Graph()

north=float(sys.argv[1]);
south=float(sys.argv[2]);
east=float(sys.argv[3]);
west=float(sys.argv[4]);
noOfBlocks=int(sys.argv[5]);
k=0;

vDist=(north-south)/noOfBlocks;
hDist=(east-west)/noOfBlocks;

for i in range(0, noOfBlocks):
    n=north-i*vDist;
    s=n-vDist;
    clat=(n+s)/2
    for j in range(0, noOfBlocks):
        w=west+j*hDist;
        e=w+hDist;
        clong=(e+w)/2
        G.add_node(str(i)+"_"+str(j), {'north':n, 'south':s, 'east':e, 'west':w, 'clat':clat, 'clong':clong, 'sentiment':0});
        k=k+1;

for i in range(0, noOfBlocks):
    for j in range(0, noOfBlocks):
        if j!=0:
            G.add_edge(str(i)+"_"+str(j), str(i)+"_"+str(j-1));

        if j!=noOfBlocks-1:
            G.add_edge(str(i)+"_"+str(j), str(i)+"_"+str(j+1));
            
        if i!=0:
            G.add_edge(str(i)+"_"+str(j), str(i-1)+"_"+str(j));
            if j!=0:
                G.add_edge(str(i)+"_"+str(j), str(i-1)+"_"+str(j-1));
            if j!=noOfBlocks-1:
                G.add_edge(str(i)+"_"+str(j), str(i-1)+"_"+str(j+1));
            
        if i!=noOfBlocks-1:
            G.add_edge(str(i)+"_"+str(j), str(i+1)+"_"+str(j));
            if j!=0:
                G.add_edge(str(i)+"_"+str(j), str(i+1)+"_"+str(j-1));
            if j!=noOfBlocks-1:
                G.add_edge(str(i)+"_"+str(j), str(i+1)+"_"+str(j+1));

            
G.to_undirected();            
nx.draw_networkx_nodes(G, pos=nx.spring_layout(G))
nx.draw_networkx_edges(G, pos=nx.spring_layout(G), alpha=0.5,width=6)
 
plt.axis('on')
plt.savefig("graph.png") # save as png
plt.show() # display

print(G.adjacency_list())
print(G.edges())
print(sorted(G.nodes()))

nx.write_gml(G, "graph.gml")
