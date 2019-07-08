import networkx as nx
from networkx.drawing.nx_agraph import write_dot, graphviz_layout
import matplotlib.pyplot as plt

def drowGraph():
    G = nx.Graph()
    G.add_nodes_from([1, 6])
    edg = [(1, 2), (2, 3), (6, 3), (5, 6), (2, 5), (2, 4), (4, 1)]
    G.add_edges_from(edg)

    # start drowing
    plt.subplot(121)
    nx.draw(G, with_labels=True, font_weight='bold')
    # plt.subplot(122)
    # nx.draw_shell(G, nlist=[range(5, 10), range(5)], with_labels=True, font_weight='bold')
    plt.show()
    return None





# DG = nx.DiGraph()
# >>> DG.add_weighted_edges_from([(1, 2, 0.5), (3, 1, 0.75)])
# >>> DG.out_degree(1, weight='weight')
# 0.5
# >>> DG.degree(1, weight='weight')
# 1.25
# >>> list(DG.successors(1))
# [2]
# >>> list(DG.neighbors(1))

import copy

PLAYER_HP = 0
OPPONENT_HP = 1

class Graph:

    def __init__(self):

        # self.vertex_id = vertex_id
        # self.connectedTo = {}
        self.G = nx.DiGraph()


    def addnode(self, vertex_id):

        self.G.add_node(vertex_id)

    def giveEdges(self, node1, node2):

        # self.connectedTo[node2] = weigth
        self.G.add_edge(node1, node2, weigth=0)

    def drawGraph(self):

        # write_dot(self.G, 'test.dot')
        # nx.draw_networkx(self.G)
        # plt.show()
        # write_dot(self.G, 'test.dot')

        # same layout using matplotlib with no labels
        plt.title('draw_networkx')
        pos = graphviz_layout(self.G, prog='dot')
        nx.draw(self.G, pos, with_labels=False, arrows=True)
        plt.show()



def take_damage(minion, damage):
    minion[0] -= damage
    if minion[0] <= 0:
        minion = [0, 0]
    return minion


def attack_minion(previous_state):
    previous_state = list(previous_state)
    attacking_minion = previous_state[2: 4]
    defending_minion = previous_state[4: 6]

    attacking_minion = take_damage(attacking_minion, defending_minion[1])
    defending_minion = take_damage(defending_minion, attacking_minion[1])

    new_state = previous_state[:2] + attacking_minion + defending_minion
    return tuple(new_state)



def attack_player(previous_state):
    previous_state = list(previous_state)
    previous_state = copy.deepcopy(previous_state)
    previous_state[1] -= previous_state[4]
    return tuple(previous_state)

def game_value(state):
    state = copy.deepcopy(state)
    if state[PLAYER_HP] > 0 and state[OPPONENT_HP] <= 0:
        return 1
    elif state[PLAYER_HP] <= 0:
        return -1
    else:
        return 0

def createGames():
    initial_state = (30, 30, 3, 4, 3, 4)
    graph = Graph()
    graph.addnode(initial_state)
    previous_states = [initial_state]
    for turn in range(3):
        next_states = set() # to avoid duplicates
        for previous_state in previous_states:
            s1 = attack_player(previous_state)
            graph.addnode(s1)
            graph.giveEdges(previous_state, s1)

            s2 = attack_minion(previous_state)
            graph.addnode(s2)
            graph.giveEdges(previous_state, s2)
            next_states.update((s1, s2))
        print(len(next_states)) # looking how many new states are found
        previous_states = [] # move new state into prev one
        for n in next_states:
            if game_value(n) == 0: # check if game is over
                previous_states.append(n)
    return graph

graph = createGames()
graph.drawGraph()
pass



