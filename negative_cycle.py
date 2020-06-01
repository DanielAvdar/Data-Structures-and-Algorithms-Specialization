# Uses python3
##############################
# @author Daniel Avdar
# @input: #edges, #vertices (one line)
#         the graph's edges (following lines)
# @output: 1 if the graph contains a cycle of negative weight and 0 otherwise
# @description: Given an directed graph with possibly negative edge weights and
#               with 𝑛 vertices and 𝑚 edges, check whether it contains
#               a cycle of negative weight
##############################

import sys


def generateDWGraph(edges, n):
    graph = {}
    for i in range(1, n + 1):
        graph[i] = [False, dict(), 10 ** 7 + 1]
    for ((a, b), w) in edges:
        graph[a][1][b] = w

    return graph


def negative_cycle(graph, edges):
    graph[1][2] = 0
    for _ in graph:
        for ((a, b), w) in edges:
            if graph[b][2] > graph[a][2] + w:
                graph[b][2] = graph[a][2] + w
    for ((a, b), w) in edges:
        if graph[b][2] > graph[a][2] + w:
            return 1
    return 0


if __name__ == '__main__':
    input_ = sys.stdin.read()
    data = list(map(int, input_.split()))
    n, m = data[0:2]
    data = data[2:]
    edges = list(zip(zip(data[0:(3 * m):3], data[1:(3 * m):3]), data[2:(3 * m):3]))
    data = data[3 * m:]
    graph = generateDWGraph(edges, n)
    print(negative_cycle(graph, edges))
# todo git
