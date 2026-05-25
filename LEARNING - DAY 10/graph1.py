# Adjanceny MAtrix

class Graph:
    def __init__(self, vertices):
        #total no of vertices
        self.V = vertices

        # create adjanceny matrix with all 0s
        self.matrix = [[0 for _ in range(vertices)]
                      for _ in range(vertices)]
        
    def display(self):
        for row in self.matrix:
            print(row)

 # add edge between two vertices
    def add_edge(self, u, v):
      self.matrix[u][v] = 1
      self.matrix[v][u] = 1  # for undirected graph

    def remove_edge(self, u, v):
      self.matrix[u][v] = 0
      self.matrix[v][u] = 0 
    
# create a graph with 4 vertices
g =Graph(4)

# add edges

g.add_edge(0,1)
g.add_edge(0,2)
g.add_edge(1,3)
g.add_edge(2,3)

g.remove_edge(2,3)

print("adjanceny matrix: ")
g.display()