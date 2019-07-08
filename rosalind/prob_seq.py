import numpy as np
import argparse

seq = 'AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB'


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='HMM')
    parser.add_argument('--seq', dest='seq', type=str)
    parser.add_argument('--states', dest='states', type=list)
    parser.add_argument('--states_prob', dest='states_prob', nargs='+', type=float)
    parser.add_argument('--tran', dest='tran',nargs='+',  type=float)

    # parser.add_argument('--tran1', dest='tran1', type=float)
    # parser.add_argument('--tran2', dest='tran2', type=float)

    args = parser.parse_args()
    return args


def hmm(seq, trans, initial_prob):
    tot = []

    for index, state in enumerate(seq):
        if index == 0:
            tot.append(initial_prob[state])
            # print(state)
        else:
            # print(state, [index - 1])
            # if index == 0: tot.append(initial_prob[state])
            tot.append(trans[(state, seq[index - 1])])

    return np.prod(tot)



args = parse_args()

print('Called with args:')
print(args)


seq_ = args.seq
transitions = {(args.states[0], args.states[1]): args.tran[0], (args.states[1], args.states[0]): args.tran[1],
               (args.states[0], args.states[0]): args.tran[2], (args.states[1], args.states[1]): args.tran[3]}
initial = {args.states[0]: args.states_prob[0], args.states[1]: args.states_prob[1]}


# AABBBAABABAAAABBBBAABBABABBBAABBAAAABABAABBABABBAB
# --------
# A   B
# --------
#     A   B
# A   0.194   0.806
# B   0.273   0.727




# seq_weather = 'DDRR'
# transitions = {('R', 'D'): 0.2, ('D', 'R'): 0.7, ('D', 'D'): 0.8, ('R', 'R'): 0.3}
# initial = {'R': 0.4, 'D': 0.6}

# trans = {('A', 'B'): ('B', 'A'): ('B', 'B'): ('A', 'A'):}
print(hmm(seq_, transitions, initial))
