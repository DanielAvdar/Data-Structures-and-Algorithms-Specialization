# Uses python3
#####################################
#
# @author Daniel Avdar
#
# @description:
# Return the trie built from reads
# in the form of a dictionary of dictionaries, e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
#
#####################################

import sys


def build_trie(patterns):
    tree_ = dict()
    tree_[0] = dict()
    new_k = 1
    for i in patterns:
        node_ = tree_.get(0)
        for j in i:
            letter = node_.get(j)
            if letter is None:
                node_[j] = new_k
                tree_[new_k] = dict()
                new_k += 1
            go_to = node_[j]
            node_ = tree_[go_to]
    return tree_


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
# todo git
