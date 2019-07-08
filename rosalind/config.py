import argparse


def parse_args():
    """
    Parse input arguments
    """
    parser = argparse.ArgumentParser(description='HMM')
    parser.add_argument('--seq', dest='seq', type=str)
    parser.add_argument('--states', dest='states', type=list)
    parser.add_argument('--states_prob', dest='states_prob', nargs='+', type=float)
    parser.add_argument('--tran', dest='tran', nargs='+', type=float)

    # parser.add_argument('--tran1', dest='tran1', type=float)
    # parser.add_argument('--tran2', dest='tran2', type=float)

    args = parser.parse_args()
    return args
