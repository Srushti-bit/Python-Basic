''''
Adjanecy Matrix:  matrix are formed based on vertices (how many vertices are present)
Adjanecy List:

on what basis adjanecy matrix and list are implemented?
 ans: based on density
 if no. of edges is less use adjanecy list and if no. of edges are more then use matrix
  (explain all these points with examples)
'''
# adjancency List

class Graph:
    def __init__(self):
        self.adjacency_list = {}

    def add_vertex(self, vertex):
        if vertex not in self.adjacency_list.keys():
            self.adjacency_list[vertex] = []
            return True
        return False
    
    def print_graph(self):
        for vertex in self.adjacency_list:
            print(vertex,":",self.adjacency_list[vertex])

    def add_edge(self, vertex1, vertex2):#(A,D)
        if vertex1 in self.adjacency_list.keys() and vertex2 in self.adjacency_list.keys():
            self.adjacency_list[vertex1].append(vertex2)
            return True
        return False
    
my_graph = Graph()
my_graph.add_vertex("A")
my_graph.add_vertex("B")
my_graph.add_vertex("C")
my_graph.add_vertex("D")
my_graph.add_vertex("E")

my_graph.add_edge("A", "E")
my_graph.add_edge("A", "C")
my_graph.add_edge("A", "D")
my_graph.add_edge("B", "A")
my_graph.add_edge("B", "E")
my_graph.print_graph()