from vertex import Vertex


class Graph:
    def __init__(self):
        self.graph_dict = {}

    def add_vertex(self, node):
        self.graph_dict[node.value] = node

    def add_edge(self, from_node, to_node, weight=0):
        self.graph_dict[from_node.value].add_edge(to_node.value, weight)
        self.graph_dict[to_node.value].add_edge(from_node.value, weight)

    def explore(self):
        print("Exploring the graph....\n")
        # FILL IN EXPLORE METHOD BELOW

    def print_map(self):
        print("\nMAZE LAYOUT\n")
        for node_key in self.graph_dict:
            print("{0} connected to...".format(node_key))
            node = self.graph_dict[node_key]
            for adjacent_node, weight in node.edges.items():
                print("=> {0}: cost is {1}".format(adjacent_node, weight))
            print("")
        print("")


def build_graph():
    graph = Graph()

    # MAKE ROOMS INTO VERTICES BELOW...
    entrance = Vertex("entrance")

    # ADD ROOMS TO GRAPH BELOW...
    graph.add_vertex(entrance)

    # ADD EDGES BETWEEN ROOMS BELOW...
    ante_chamber = Vertex("ante-chamber")
    graph.add_vertex(ante_chamber)
    kings_room = Vertex("king's room")
    graph.add_vertex(kings_room)

    graph.add_edge(entrance, ante_chamber, 7)
    graph.add_edge(entrance, kings_room, 3)

    graph.add_edge(kings_room, ante_chamber, 1)
    grand_gallery = Vertex("grand_gallery")
    graph.add_vertex(grand_gallery)

    graph.add_edge(grand_gallery, ante_chamber, 2)

    graph.add_edge(grand_gallery, kings_room, 2)

    treasure_room = Vertex("treasure_room")
    graph.add_vertex(treasure_room)

    # DON'T CHANGE THIS CODE
    graph.print_map()
    return graph