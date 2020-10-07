import numpy as np
import time

output = []

def readData(filename):
    with open(filename, "r") as f:
        Nvertex = int(f.readline())
        Nedges = int(f.readline())
        result = [[] for i in range(Nvertex)]
        for i in range(Nedges):
            s, t = [int(x) for x in f.readline().split()]
            result[s].append(t)
    return result

def dfs(node, graph, record):
    if record[node] == 1:
        return 1
    else:
        record[node] = 1
    for index in range(len(graph[node])):
        i = graph[node][index]
        tmp = np.array(record)
        result = dfs(i, graph, record)
        record = tmp.tolist()
        if result == 1:
            if (node, i) not in output:
                print("cycle detect!!")
                print("remove edge of {} to {}".format(node, i))
                graph[node].pop(index)
                output.append((node,i))
    return 0

graph = readData("input1.dat")
for i in range(len(graph)):
    record = [0 for i in range(len(graph))]
    dfs(i, graph, record)
print('input1 done')
print('--------------')
graph = readData("input2.dat")
for i in range(len(graph)):
    record = [0 for i in range(len(graph))]
    dfs(i, graph, record)
print('input2 done')
