# five elements for HMM
states = ('A', 'B')

observations = ('x', 'y', 'z')

start_probability = {'A': 0.5, 'B': 0.5}

transition_probability = {
    'A': {'A': 0.634, 'B': 0.387},
    'B': {'A': 0.366, 'B': 0.613},
}

emission_probability = {
    'A': {'x': 0.532, 'y': 0.226, 'z': 0.241},
    'B': {'x': 0.457, 'y': 0.192, 'z': 0.351},
}

# seq = 'zxxxxyzzxyxyxyzxzzxzzzyzzxxxzxxyyyzxyxzyxyxyzyyyyzzyyyyzzxzxzyzzzzyxzxxxyxxxxyyzyyzyyyxzzzzyzxyzzyyy'

obs = 'zxxxxyzzxyxyxyzxzzxzzzyzzxxxzxxyyyzxyxzyxyxyzyyyyzzyyyyzzxzxzyzzzzyxzxxxyxxxxyyzyyzyyyxzzzzyzxyzzyyy'
# A	B
# A	0.634	0.366
# B	0.387	0.613
# --------
# 	x	y	z
# A	0.532	0.226	0.241
# B	0.457	0.192	0.351


# Output:
# AAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBAAA


#
output = 'AAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBBAAAAAAAAAAAAAAAAAAAAABBBBBBBBBBAAA'


def Viterbit(obs, states, s_pro, t_pro, e_pro):
    path = {s: '' for s in states}  # init path: path[s] represents the path ends with s
    curr_pro = {}
    for s in states:
        curr_pro[s] = s_pro[s] * e_pro[s][obs[0]]
    for i in range(1, len(obs)):
        last_pro = curr_pro
        curr_pro = {}
        for curr_state in states:
            max_pro, last_sta = max(
                ((last_pro[last_state] * t_pro[last_state][curr_state] * e_pro[curr_state][obs[i]], last_state)
                 for last_state in states))
            curr_pro[curr_state] = max_pro
            # path[curr_state].append(last_sta)
            path[curr_state] += last_sta

    # find the final largest probability
    max_pro = -1
    max_path = None
    for s in states:
        path[s] += s
        # path[s].append(s)
        if curr_pro[s] > max_pro:
            max_path = path[s]
            max_pro = curr_pro[s]
    # print '%s: %s'%(curr_pro[s], path[s]) # different path and their probability
    # assert max_path == output
    return max_path


# Helps visualize the steps of Viterbi.
def print_dptable(V):
    s = "    " + " ".join(("%7d" % i) for i in range(len(V))) + "\n"
    for y in V[0]:
        s += "%.5s: " % y
        s += " ".join("%.7s" % ("%f" % v[y]) for v in V)
        s += "\n"
    # print(s)


def viterbi(obs, states, start_p, trans_p, emit_p):
    V = [{}]
    path = {}

    # Initialize base cases (t == 0)
    for y in states:
        V[0][y] = start_p[y] * emit_p[y][obs[0]]
        path[y] = [y]

    # alternative Python 2.7+ initialization syntax
    # V = [{y:(start_p[y] * emit_p[y][obs[0]]) for y in states}]
    # path = {y:[y] for y in states}

    # Run Viterbi for t > 0
    for t in range(1, len(obs)):
        V.append({})
        newpath = {}

        for y in states:
            (prob, state) = max((V[t - 1][y0] * trans_p[y0][y] * emit_p[y][obs[t]], y0) for y0 in states)
            V[t][y] = prob
            newpath[y] = path[state] + [y]

        # Don't need to remember the old paths
        path = newpath

    print_dptable(V)
    (prob, state) = max((V[t][y], y) for y in states)
    return (prob, path)


def example():
    return viterbi(observations,
                   states,
                   start_probability,
                   transition_probability,
                   emission_probability)


print(example())

if __name__ == '__main__':
    # obs = ['x', 'y', 'dizzy']
    print(Viterbit(obs, states, start_probability, transition_probability, emission_probability))
