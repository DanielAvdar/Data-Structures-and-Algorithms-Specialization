# Uses python3
##############################
# @author Daniel Avdar
# @input: #edges, #vertices (one line)
#         the graph's edges (following lines)
#         the vertices u,v to find the path between them (last line)
# @output: the minimum number of edges in a path from 𝑢 to 𝑣,
#          or −1 if there is no path.
# @description: bfs algorithm for finding the shortest path in a graph
#
##############################

import sys
import queue

q = queue.Queue()
from numpy import inf


def generate_DWG_raph(edges, n):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = [False, dict(), False, [inf, i]]
    for (a, b) in edges:
        graph[a][1][b] = 1
        graph[b][1][a] = 1
    return graph


def distance(graph, s, t):
    qu = queue.Queue()

    def set_v(v, w):
        graph[v][3][0] = min(w, graph[v][3][0])

    set_v(s, 0)
    qu.put(graph[s][3])
    graph[s][2] = True
    while not qu.empty():
        w, v = qu.get()
        graph[v][0] = True
        for i in graph[v][1].keys():
            if graph[i][0]:
                continue

            set_v(i, w + graph[v][1][i])
            if graph[i][2]:
                continue
            graph[i][2] = True
            qu.put(graph[i][3])

    return graph[t][3][0] if graph[t][3][0] != inf else -1


def main():
    input = sys.stdin.read()
    data = list(map(int, input.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(data[0:(2 * m):2], data[1:(2 * m):2]))
    g = generate_DWG_raph(edges, n)
    if not data:
        print(-1)
        return
    s, t = data[-2], data[-1]
    print(distance(g, s, t))


if __name__ == '__main__':
    main()
# todo git
