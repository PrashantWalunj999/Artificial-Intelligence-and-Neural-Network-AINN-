# AI—Teaching Pacman To Search With Depth First Search
# The Example is solved in ( Python 3.6 )
#	
#	Y ______
#	4|  __  |   c = Current Place of pacman
#	3| | d| |   d = Destination
#	2|  __| |   start state (1,1) to a goal state (2,3)
#  	1|c_____|
#	  1 2 3 4 X

from queue import PriorityQueue

def dfs(graph, start, goal):
	# initialise visited list, path list & fringe
    # Add starting node to the fringe
    visited = []
    path = []
    fringe = PriorityQueue()
    fringe.put((0, start, path, visited))

    # While there are still nodes in the fringe, keep exploring!
    while not fringe.empty():
        # 1. Remove the next most prioritised node from the fringe
        depth, current_node, path, visited = fringe.get()

        # 2. Check to see if it is the goal node
        if current_node == goal:
            return path + [current_node]

        # 3. Add to our list of explored nodes
        visited = visited + [current_node]

        # If not goal, get its child nodes
        child_nodes = graph[current_node]
        # 4. Add child nodes to the fringe if they haven't been visited yet
        for node in child_nodes:
            if node not in visited:
                if node == goal:
                    return path + [node]
                depth_of_node = len(path)
 # The priority queue prioritises lower values over higher ones (i.e. 1 is prioritised higher than 10)
                # Since we are using depth of node as our prioritisation measure we need to pass in negative priorities
                # To ensure that nodes with greater depth get explored before shallower ones
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


### ::::OUTPUT::::
'''	
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/TYB350/Sem1/ainn/lab/assignment1$ python3 pacman.py
path [(1, 2), (2, 2), (2, 3)]
PrashantWalunj@PrashantWalunj:/mnt/e/Prashant/TYB350/Sem1/ainn/lab/assignment1$
'''
