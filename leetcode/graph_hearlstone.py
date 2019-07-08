import copy

PLAYER_HP = 0
OPPONENT_HP = 1

class Vertex:

    def __init__(self, vertex_id):

        self.vertex_id = vertex_id
        self.connectedTo = {}

    def giveEdges(self, weigth, node2):

        self.connectedTo[node2] = weigth


def take_damage(minion, damage):
    minion[0] -= damage
    if minion[0] <= 0:
        minion = [0, 0]
    return minion


def attack_minion(previous_state):
    attacking_minion = previous_state[2: 4]
    defending_minion = previous_state[4: 6]

    attacking_minion = take_damage(attacking_minion, defending_minion[1])
    defending_minion = take_damage(defending_minion, attacking_minion[1])

    new_state = previous_state[:2] + attacking_minion + defending_minion
    return new_state



def attack_player(previous_state):
    previous_state = copy.deepcopy(previous_state)
    previous_state[1] -= previous_state[4]
    return previous_state

def game_value(state):
    state = copy.deepcopy(state)
    if state[PLAYER_HP] > 0 and state[OPPONENT_HP] <= 0:
        return 1
    elif state[PLAYER_HP] <= 0:
        return -1
    else:
        return 0

def createGames():
    initial_state = [30, 30, 3, 4, 3, 4]
    initial_node = Vertex(initial_state)

    previous_nodes = [initial_node]
    for turn in range(3):
        next_nodes = []
        for previous_node in previous_nodes:
            s1 = attack_player(initial_state)
            n1 = Vertex(s1)
            previous_node.giveEdges(0, n1)

            s2 = attack_minion(initial_state)
            n2 = Vertex(s2)
            previous_node.giveEdges(0, n2)
            next_nodes.extend((n1, n2))
        print(len(next_nodes))
        for n in next_nodes:
            print("the n.vestex_id is " + str(n.vertex_id))
            if game_value(n.vertex_id) == 0:
                previous_nodes.append(n)
    return initial_node

root = createGames()
pass
