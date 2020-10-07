# r08944028 賴達
import sys

def dfs_visit(vertex, adjlist, color, remove_edges):
	color[vertex] = 1
	isdag = True
	for i in adjlist[vertex]:
		if color[i] == 1:
			isdag = False
			remove_edges.append([vertex,i])
		if color[i] == 0 and dfs_visit(i, adjlist, color, remove_edges) == False:
			isdag = False
	color[vertex] = 2
	return isdag

if __name__ == '__main__' :
	file = open(str(sys.argv[1]), 'r')
	vertex_num, edge_num, remove_edges = int(file.readline().strip()), int(file.readline().strip()), []
	color, adjlist = [0]*vertex_num, [[] for i in range(vertex_num)]
	for i in range(edge_num):
		a, b = map(int,file.readline().strip().split())
		adjlist[a].append(b)
	isdag = True
	for i in range(vertex_num):
		if color[i] == 0 and dfs_visit(0, adjlist, color, remove_edges) == False:
			isdag = False
	if isdag:
		print('Graph is acyclic')
	else:
		print('Graph is cyclic\nneed to remove edges', remove_edges)