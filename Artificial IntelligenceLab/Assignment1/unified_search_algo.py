# AI—Teaching Pacman To Search With Depth First Search
# The Example is solved in ( Python 3.6 )

from queue import PriorityQueue

def dfs(graph, start, goal):
    visited = []
    path = []
    fringe = PriorityQueue()
    fringe.put((0, start, path, visited))

    while not fringe.empty():
        depth, current_node, path, visited = fringe.get()

        if current_node == goal:
            return path + [current_node]

        visited = visited + [current_node]

        child_nodes = graph[current_node]
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
                fringe.put((-depth_of_node, node, path + [node], visited))

    return path

if __name__ == "__main__":
    graph = {
        (1,1): set([(1,2), (2,1)]),
        (1,2): set([(2,2), (1,3)]),
        (1,3): set([(1,4), (1,2)]),
        (1,4): set([(1,3), (2,4)]),
        (2,1): set([(1,1), (1,3)]),
        (2,2): set([(2,3), (1,2)]),
        (2,3): set([(2,2)]),
        (2,4): set([(1,4), (3,4)]),
        (3,1): set([(2,1), (3,2)]),
        (3,2): set([(3,1), (3,3)]),
        (3,3): set([(3,2), (3,4)]),
        (3,4): set([(2,4), (3,3)]),
    }

    path = dfs(graph, (1,1), (2,3))
    print("path", path) # ==> [(1,2), (2,2), (2,3)]

    #:::output:::

#PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/TYB350/Sem1/ainn/lab/Assignment1$ python3 unified_search_algo.py
#path [(1, 2), (2, 2), (2, 3)]
#PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/TYB350/Sem1/ainn/lab/Assignment1$