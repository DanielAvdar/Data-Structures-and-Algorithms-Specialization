# python3
##############################
#
# @author Daniel Avdar
#
# @description:Extend TrieMatching algorithm so that it
#              handles correctly cases when one of the
#              patterns is a prefix of another one.
#
# @input: The first line of the input contains a string Text,
#         the second line contains the number of patterns,
#         and the following lines contain the patterns
#
# @output:All starting positions in Text where a string
#         from Patterns appears as a substring in
#         increasing order (assuming that Text is a
#         0-based array of symbols).
#         If more than one pattern appears starting at
#         position 𝑖, output 𝑖 once.
#
##############################


import sys

NA = -1
HIT = "hit"


def build_trie(patterns):
    tree = dict()
    tree[0] = dict()
    new_k = 1

    prev = None
    for i in patterns:
        node = tree.get(0)
        j = 0
        for j in i:
            letter = node.get(j)
            if letter is None:
                node[j] = new_k
                tree[new_k] = dict()
                new_k += 1

            go_to = node[j]
            prev = node
            node = tree[go_to]
        if prev.get(HIT) is None:
            prev[HIT] = set()
        prev[HIT].add(j[len(j) - 1])
    return tree


def solve(text, patterns):
    result = []

    tree = build_trie(patterns)

    def find_patt(ind, node_ind=0, c=0):
        node = tree[node_ind]
        if ind + c == len(text):
            return
        node_ind = node.get(text[ind + c])
        if node_ind is None:
            return
        hit = node.get(HIT)
        if hit is not None and text[ind + c] in hit:
            result.append(ind)
            return

        find_patt(ind, node_ind, c + 1)

    for ind in range(len(text)):
        find_patt(ind)

    return list(result)


def main():
    text = sys.stdin.readline().strip()
    n = int(sys.stdin.readline().strip())
    patterns = []
    for i in range(n):
        patterns += [sys.stdin.readline().strip()]

    ans = solve(text, patterns)

    sys.stdout.write(' '.join(map(str, ans)) + '\n')


if __name__ == '__main__':
    main()

# todo git
