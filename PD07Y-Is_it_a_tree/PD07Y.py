import fileinput
from collections import defaultdict


class Graph:
    def __init__(self, V):
        self.V = V
        self.graph = defaultdict(list)

    def addEdge(self, v, w):
        # Add w to v ist.
        self.graph[v].append(w)
        # Add v to w list.
        self.graph[w].append(v)

    # A recursive function that uses visited[] and parent to detect cycle in subgraph reachable from vertex v.
    def isCyclicUtil(self, v, visited, parent):
        # Mark current node as visited
        visited[v] = True

        # Recur for all the vertices adjacent for this vertex
        for i in self.graph[v]:
            # If an adjacent is not visited, then recur for that adjacent
            if not visited[i]:
                if self.isCyclicUtil(i, visited, v):
                    return True

            # If ana adjacent is visited and not parent of current vertex, then there is a cycle
            elif i != parent:
                return True

        return False

    # Returns true if the graph is a tree, else false
    def isTree(self):
        # Mark all the vertices as not visited and not part of recursion stack
        visited = [False] * self.V

        # The call to isCyclicUtil serves multiple purpose.
        # It returns true if graph reachable from vertex 0 is cyclic.
        # It also marks all vertices reachable from 0.
        if self.isCyclicUtil(0, visited, -1):
            return False

        # If we find a vertex which is not reachable from 0 (not marked by isCyclicUtil(), then we return false
        for i in range(self.V):
            if not visited[i]:
                return False

        return True


# Test data
test_data_1 = ['3 2',
               '1 2',
               '2 3']

test_data_2 = ['5 4',
               '1 3',
               '1 4',
               '4 2',
               '2 5']

test_data_3 = ['5 3',
               '1 3',
               '1 4',
               '2 5']

test_data_4 = ['5 4',
               '1 3',
               '1 4',
               '2 5',
               '3 4']

test_data_5 = ['5 5',
               '1 3',
               '1 4',
               '4 2',
               '2 5',
               '3 4']

test_data_6 = ['5 4',
               '1 0',
               '0 2',
               '0 3',
               '3 4']

# Standard input()
entree_str = [line.strip() for line in fileinput.input()]

# entree_str = test_data_6

Node, Edge = entree_str[0].split(' ')
if int(Node) - int(Edge) != 1:
    print('NO')
else:
    g1 = Graph(int(Node))

    for i in range(len(entree_str) - 1):
        edge_list = entree_str[i + 1].split(' ')
        g1.addEdge(int(edge_list[0])-1, int(edge_list[1])-1)

    print('YES' if g1.isTree() else 'NO')

# Test
# g1 = Graph(5)
# g1.addEdge(1, 0)
# g1.addEdge(0, 2)
# g1.addEdge(0, 3)
# g1.addEdge(3, 4)
#
# print(g1.isTree())
