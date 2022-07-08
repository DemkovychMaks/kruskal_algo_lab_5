class Graph:

    def __init__ (self, V):
        self.V = V
        self.edges = []
        self.mst = []
        self.rank = [0] * self.V
        self.parent = [vertex for vertex in range(self.V)]

    def add_edge(self, vertex_start, vertex_end, weight):
        self.edges.append([vertex_start, vertex_end, weight])

    def find_root(self, vertex):
        if vertex == self.parent[vertex]:
            return vertex
        else:
            return self.find_root(self.parent[vertex])

    def union(self, first_root, second_root, edge):
        if self.rank[first_root] < self.rank[second_root]:
            self.parent[first_root] = second_root
            self.rank[second_root] += 1
        else:
            self.parent[second_root] = first_root
            self.rank[first_root] += 1

    def kruskal(self):
        print(self.rank)
        def take_weight(e):
            return e[2]
        sorted_edges = sorted(self.edges, key = take_weight)
        for edge in sorted_edges:
            first_root = self.find_root(edge[0])
            second_root = self.find_root(edge[1])
            if first_root != second_root:
                self.mst.append(edge)
                self.union(first_root, second_root, edge)
        print(self.rank)
        print(self.parent)



g = Graph(6)
g.add_edge(0, 1, 10)
g.add_edge(1, 2, 12)
g.add_edge(1, 3, 7)
g.add_edge(2, 3, 12)
g.add_edge(2, 4, 10)
g.add_edge(3, 4, 300)
g.add_edge(3, 5, 6)
g.kruskal()
print(g.mst)

result = 0
for edge in g.mst:
    result += edge[2]
print(result)