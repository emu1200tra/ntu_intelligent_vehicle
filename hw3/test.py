import numpy as np
import networkx as nx
import matplotlib.pyplot as plt

def readData(filename):
    with open(filename, "r") as f:
        Nvertex = int(f.readline())
        Nedges = int(f.readline())
        result = []
        for i in range(Nedges):
            x,y = f.readline().split()
            result.append((x,y))
    return result, Nvertex, Nedges

graph, Nvertex, Nedges = readData("input2.dat")
G = nx.from_edgelist(graph)
index = [int(i) for i in G.nodes()]
labelmap = dict(zip(G.nodes(), index))
nx.draw(G, labels=labelmap, with_labels=True)
plt.show()

