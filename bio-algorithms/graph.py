class Graph():

    def __init__(self):
        self.graph = {}

    def showVertices(self):
        return list(self.graph.keys())

    def showEdges(self):
        return self.toupleEdges()

    def addVertex(self, *verteces):
        for vertex in verteces:
            if vertex not in self.graph:
                self.graph[vertex] = []

    def addEdge(self, src, *args):
        try:
            self.graph[src].append(*args)
        except:
            self.graph[src] = [*args]

    def toupleEdges(self):
        edges = list()
        for node in self.graph:
            # the edges or other nodes connected to current node
            for neighbour in graph[node]:
                edges.append((node, neighbour))
        return edges


start = Graph()
start.addVertex("a", "b", "c", "d", "e", "f")
start.addEdge("a", "c")
start.addEdge("b", "c", "e")
start.addEdge("c", "a", "b", "d", "e")
start.addEdge("d", "c")
start.addEdge("e", "c", "b")

"""
graph = {"a": ["c"],
         "b": ["c", "e"],
         "c": ["a", "b", "d", "e"],
         "d": ["c"],
         "e": ["c", "b"],
         "f": []
         }
"""
