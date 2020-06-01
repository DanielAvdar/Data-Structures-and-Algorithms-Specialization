# python3
##############################
#
# @author Daniel Avdar
#
# @description: A k-universal circular string is a circular string that
#              contains every possible k-mer constructed over a given alphabet.
#
# @input: An integer k.
#
# @Constraints: 3<k<15.
#
# @output: A k-universal circular string.
#
##############################
import threading
import collections
import sys

sys.setrecursionlimit(8 ** 10)
threading.stack_size(2 ** 27)
Vertex = collections.namedtuple('Vertex',
                                ["neighbors", "self", "num_of_outs",
                                 "num_of_ins"])


def dfs(graph, vertex, func):
    while graph[vertex].num_of_outs > 0:
        neighbor_ind = len(graph[vertex].neighbors) - graph[
            vertex].num_of_outs
        neighbor = graph[graph[vertex].neighbors[neighbor_ind]].self
        graph[vertex] = graph[vertex]._replace(
            num_of_outs=graph[vertex].num_of_outs - 1)
        dfs(graph, neighbor, func)
    func(vertex)


def find_start(graph):
    start_v = 1
    for i in graph:
        outs = graph[i].num_of_outs
        ins = graph[i].num_of_ins
        if outs != ins:
            return 0
    return start_v


def build_graph(graph, start):
    if graph.get(start) is not None:
        return
    tmp = [start[1:] + '1', start[1:] + '0']
    graph[start] = Vertex._make([tmp, start, 2, 2])
    build_graph(graph, tmp[0])
    build_graph(graph, tmp[1])


def get_graph(n):
    graph = dict()
    build_graph(graph, "0" * (n - 1))
    return graph


def find_OC(n):
    graph = get_graph(n)
    if graph is None:
        return 0
    tmp_res = []

    def func(v):
        tmp_res.append(v)

    dfs(graph, "0" * (n - 1), func)
    tmp_res = tmp_res[::-1][:len(tmp_res) - 1]
    res = "0" * n
    for i in tmp_res[1:len(tmp_res) - n + 1]:
        res += i[n - 2]
    return res


def main():
    res = find_OC(int(input()))
    print(res)


threading.Thread(target=main).start()
# todo git
