# Uses python3
##############################
# @author Daniel Avdar
# @input: #edges, #vertices (one line)
#         the graph's edges (following lines)
#         the vertices s,t to find the path between them (last line)
# @output: the minimum weight of a path from s to t,
#          or −1 if there is no path.
# @description: Dijkstra algorithm for finding the shortest path in a weighted graph
#
##############################

import sys
import heapq
from numpy import inf

heap = []


def generateDWGraph(edges, n):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = [False, dict(), None, [inf, i]]
        heap.append(graph[i][3])
    for ((a, b), w) in edges:
        graph[a][1][b] = w

    return graph


def distance(graph, s, t):
    heap_ = heap

    def set_v(v, w):
        graph[v][3][0] = min(w, graph[v][3][0])

    set_v(s, 0)
    heapq.heapify(heap_)

    while heap_:
        w, v = heapq.heappop(heap_)
        graph[v][0] = True
        for i in graph[v][1].keys():
            if graph[i][0]:
                continue
            set_v(i, w + graph[v][1][i])
        heapq.heapify(heap_)
    return graph[t][3][0] if graph[t][3][0] != inf else -1


def main():
    input_ = sys.stdin.read()
    data = list(map(int, input_.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))

    if not data:
        print(0)
        return

    s, t = data[-2], data[-1]
    g = generateDWGraph(edges, n)
    print(distance(g, s, t))


if __name__ == '__main__':
    main()
# todo git
