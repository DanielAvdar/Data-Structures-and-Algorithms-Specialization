# python3
##############################
#
# @author Daniel Avdar
#
# @description:In this problem, you will apply an algorithm for finding
#              maximum flow in a network to determine how fast people can
#              be evacuated from the given city.
#
# @input: a flow network
#
# @output:Output a single integer — the maximum number of people
#         that can be evacuated from the city number 1 each hour.
#
# @Constraints:1≤𝑛≤100; 0≤𝑚≤10 000; 1≤𝑢, 𝑣≤𝑛; 1≤𝑐≤10 000.  It is guaranteed
#              that 𝑚·EvacuatePerHour≤2·108, where  EvacuatePerHour is the
#              maximum number of people that can be evacuated from the
#              city each hour — the number which you need to output.
#
##############################
import queue


class Edge:

    def __init__(self, u, v, capacity, not_rev=True):
        self.from_ = u
        self.to = v
        self.capacity = capacity
        self.flow = 0
        self.not_rev = not_rev


class FlowGraph:

    def __init__(self, n):
        self.edges = []
        self.graph = [[] for _ in range(n)]

    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0, False)
        self.graph[from_].append(len(self.edges))
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    def size(self):
        return len(self.graph)

    def get_ids(self, from_):
        return self.graph[from_]

    def get_edge(self, id):
        return self.edges[id]

    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        self.edges[id ^ 1].flow -= flow


def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph


def get_bottleneck(graph, path, to):
    ed = graph.get_edge(path[to])
    bottleneck = float('inf')

    while ed is not None:

        bottleneck = min(bottleneck, ed.capacity - ed.flow)

        if path[ed.from_] is None:
            break
        ed = graph.get_edge(path[ed.from_])
    return bottleneck


def add_flow_to_path(graph, path, to, bottleneck):
    ed = graph.get_edge(path[to])
    c_id = path[to]
    while ed is not None:
        graph.add_flow(c_id, bottleneck)
        c_id = path[ed.from_]
        if path[ed.from_] is None:
            break
        ed = graph.get_edge(path[ed.from_])


def bfs(graph, from_, to):
    n = graph.size()
    path = [None] * n
    q = queue.Queue()
    q.put(from_)
    while not q.empty():
        curr_node_id = q.get()

        for id in graph.get_ids(curr_node_id):
            curr_edge = graph.get_edge(id)

            not_done_yet = path[curr_edge.to] is None and \
                           from_ != curr_edge.to and \
                           curr_edge.capacity - curr_edge.flow > 0

            if not_done_yet:
                path[curr_edge.to] = id
                q.put(curr_edge.to)

    if path[to] is None:
        return None
    return path


def max_flow(graph, from_, to):
    flow = 0

    while True:
        path = bfs(graph, from_, to)
        if path is None:
            break
        bottleneck = get_bottleneck(graph, path, to)
        add_flow_to_path(graph, path, to, bottleneck)
        flow += bottleneck

    es = graph.get_ids(from_)
    sum_ = 0
    for i in es:
        e = graph.get_edge(i)

        sum_ += e.flow

    return flow


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
    1
    >>> test("08")
    1
    >>> test("09")
    1
    >>> test("10")
    1
    >>> test("11")
    1
    >>> test("12")
    1
    >>> test("13")
    1
    >>> test("14")
    1
    >>> test("15")
    1
    >>> test("16")
    1
    >>> test("17")
    1
    >>> test("18")
    1
    >>> test("19")
    1
    >>> test("20")
    1
    >>> test("21")
    1
    >>> test("22")
    1
    >>> test("23")
    1
    >>> test("24")
    1
    >>> test("25")
    1
    >>> test("26")
    1
    >>> test("27")
    1
    >>> test("28")
    1
    >>> test("29")
    1
    >>> test("30")
    1
    >>> test("31")
    1
    >>> test("32")
    1
    >>> test("33")
    1
    >>> test("34")
    1
    >>> test("35")
    1
    >>> test("36")
    1
    """
    f = open(filename)

    lines = f.readlines()

    vertex_count, edge_count = map(int, lines[0].split())
    graph = FlowGraph(vertex_count)
    for i in lines[1:]:
        u, v, capacity = map(int, i.split())
        graph.add_edge(u - 1, v - 1, capacity)
    f.close()
    f = open(filename + ".a")
    lines = f.readlines()
    expected = int(lines[0].split()[0])
    f.close()
    res = max_flow(graph, 0, graph.size() - 1)
    pass_ = res == expected
    return 1 if pass_ else res


if __name__ == '__main__':
    graph = read_data()
    print(max_flow(graph, 0, graph.size() - 1))
# todo git
