from collections import defaultdict

from collections import deque

 

# adjacency list for the graph

graph = defaultdict(list)

 

# queue for bfs

q = deque()

 

# distances of nodes

dist = {}

 

# init sample graph

for edge in [[1,2], [1,7], [1,8], [2,3], [2,6], [3,4], [3,5], [8,9], [8,12], [9,10], [9,11]]:

    graph[edge[0]].append(edge[1])

    graph[edge[1]].append(edge[0])

 

# breadth-first search

dist[1] = 0

q.append(1)

while q:

    u = q.popleft()

    for v in graph[u]:
	print(graph[u])
	print(v)

        if v not in dist:

            q.append(v)

            dist[v] = dist[u] + 1

 

# print distances

print "Distances: "

for k, v in dist.iteritems():

    print "Distance of Node {0}: {1}".format(k, v)
