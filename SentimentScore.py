import sys
import re
import networkx as nx
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
import os.path

def assignSentiment(n, G, effectiveScore):
    effectiveScore[int(n)]=0
    if os.path.isfile("sentiments/sentiments_tips_"+str(n)):
        for line in open("sentiments/sentiments_tips_"+str(n), "r"):
            line=line.rstrip('\n')
            line=line.lstrip('  ')
            l=line.split('  ')
#             print line
#             print(str(l[0])+" "+str(l[1])+" "+str(l[2])+" "+str(l[3])+" "+str(l[4]))
            effectiveScore[int(n)]=effectiveScore[int(n)]+(float(str(l[0]))*-2)+(float(str(l[1]))*-1)+(float(str(l[2])))+(float(str(l[3]))*2)+(float(str(l[4]))*3)
    
    


for line in open(str(sys.argv[1]), "r"):
    line=line.rstrip('\n')
    if 'tips_' in line:
        l=line.split(':')
        fo=open("sentiments/sentiments_"+l[0], "a")
    else:
        l=line.split()
        if len(l)==5:
            print l[0][0]
            if l[0][0]=='0':
                fo.write(line+"\n")
                fo.close()

G=nx.Graph()
G = nx.read_gml("graph.gml")

effectiveScore={}
for n in G.nodes():
    assignSentiment(n, G, effectiveScore)
    
print effectiveScore

for k, v in sorted(effectiveScore.items()):
    G.node[k]['sentiment'] = float(v)

nx.write_gml(G, "UpdatedGraph.gml")
