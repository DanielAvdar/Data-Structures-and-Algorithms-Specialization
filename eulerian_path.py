# python3
##############################
#
# @author Daniel Avdar
#
# @description: Finds the Eulerian cycles in the graph and returns an Eulerian Path.
#               That is used for a (circular) genome, that spells Eulerian cycles in
#               the de Bruijn graph constructed on all k-mers of the genome.
#
# @input:The first line contains integers n and m— the number of vertices
#        and the number of edges,respectively.
#        Each of the following m lines specifies an edge in the format “u
#        v”. (As usual, we assume that the vertices of the graph
#        are {1,2,...,n}.) The graph may contain self-loops
#        (that is, edges of the form(v,v)) and parallel edges
#        (that is, several copies of the same edge).
#        It is guaranteed that the graph is strongly connected.
#
# @output:If the graph has no Eulerian cycle, output 0.
#         Otherwise output 1 in the first line and a sequence v1,v2,...,vm
#         of vertices in the second line - the given path.
#
##############################
import threading
import collections
import sys

sys.setrecursionlimit(8 ** 10)
threading.stack_size(2 ** 27)

Vertex = collections.namedtuple('Vertex',
                                ["visited", "neighbors", "self", "num_of_outs", "num_of_ins"])  # "back_neighbors"


def dfs(graph, vertex, func):
    while graph[vertex].num_of_outs > 0:
        neighbor_ind = len(graph[vertex].neighbors) - graph[vertex].num_of_outs
        neighbor = graph[graph[vertex].neighbors[neighbor_ind]].self
        graph[vertex] = graph[vertex]._replace(num_of_outs=graph[vertex].num_of_outs - 1)
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


def build_graph(edges, max_v_num):
    graph = dict()
    for i in range(1, max_v_num + 1):
        graph[i] = Vertex._make([False, list(), i, 0, 0])
    for e in edges:
        graph[e[0]].neighbors.append(e[1])
        graph[e[0]] = graph[e[0]]._replace(num_of_outs=graph[e[0]].num_of_outs + 1)
        graph[e[1]] = graph[e[1]]._replace(num_of_ins=graph[e[1]].num_of_ins + 1)
    start_v = find_start(graph)
    if start_v == 0:
        return None
    return graph


def inputer():
    data = sys.stdin.read().split()
    data = list(map(lambda i: (int(data[i]), int(data[i + 1])), range(0, len(data) - 1, 2)))
    n, edges_num = data[0]
    return n, edges_num, data[1:]


def find_eulerian_path(n, data):
    graph = build_graph(data, n)
    if graph == None:
        return 0
    tmp_res = []

    def func(v):
        tmp_res.append(v)

    dfs(graph, graph[1].self, func)
    tmp_res = tmp_res[:len(tmp_res) - 1][::-1]
    return 1, tmp_res


def test(filename):
    """
    >>> test("01")
    1
    >>> test("02")
    1
    >>> test("03")
    1
    >>> test("04")
    1
    >>> test("05")
    1
    >>> test("06")
    1
    >>> test("07")
    """
    f = open(filename)

    lines = f.readlines()

    n, m = map(int, lines[0].split())

    adj_matrix = [list(map(int, i.split())) for i in lines[1:]]

    f.close()
    f = open(filename + ".a")
    lines = f.readlines()
    expected1 = list(map(int, lines[0].split()))[0]
    expected2 = None
    if expected1:
        expected2 = list(map(int, lines[1].split()))
    f.close()
    exist = find_eulerian_path(n, adj_matrix)
    res = None
    if exist is not 0:
        exist, res = exist

    pass_ = exist == expected1 and res == expected2
    return 1 if pass_ else res


def main():
    n, Edges_num, data = inputer()
    res = find_eulerian_path(n, data)
    if res == 0:
        print(res)
        return
    print(res[0])
    for i in res[1]:
        print(i, end=' ')


threading.Thread(target=main).start()
# todo git
