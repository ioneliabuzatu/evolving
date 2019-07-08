import numpy as np
import argparse

parser = argparse.ArgumentParser(description='HMM')
parser.add_argument('--strings', dest='strings', type=list)  # x,y,z
parser.add_argument('--states', dest='states', type=list)
parser.add_argument('--tran', dest='tran', nargs='+', type=float)
args = parser.parse_args()

print('Called with args:')
print(args)


def hmm(seq, hidden, trans):  # Pr(x|π)

    tot = []

    for pair in zip(seq, hidden):
        print(pair)

        tot.append(trans[pair])

    return np.prod(tot)


seq = 'xxxyxyzyxzzyxzyzzzxxyzyxxzxzxxxyzzyzxxzyxyxzzzxxyx'
# --------
# x	y	z
# --------
hidden = 'ABABBBABBBBBAAAAABAAABAAABBBAAABABAABAAAAABBBABBBB'
# --------
# A	B
# --------
# 	x	y	z
# A	0.367	0.592	0.042
# B	0.176	0.226	0.598

transitions = {(args.strings[0], args.states[0]): args.tran[0], (args.strings[0], args.states[1]): args.tran[1],
               (args.strings[1], args.states[0]): args.tran[2], (args.strings[1], args.states[1]): args.tran[3],
               (args.strings[2], args.states[0]): args.tran[4], (args.strings[2], args.states[1]): args.tran[5]}

print(transitions)
print(hmm(seq, hidden, transitions))
