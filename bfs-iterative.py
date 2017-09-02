"""Not preferred implementation"""

import collections

class Edge(object):
    def __init__(self, src=None, dest=None):
        self.src = src
        self.dest = dest

class Graph(object):
    """undirected graph"""
    def __init__(self, edges=None):
        self.nvertices = 15
        self.visited = collections.defaultdict(bool)
        self.adjvertices = collections.defaultdict(list)
        for edge in edges:
            self.adjvertices[edge.src].append(edge.dest)
            self.adjvertices[edge.dest].append(edge.src)

class BFS(object):
    def search(self, graph, vertex):
        queue = collections.deque()
        queue.appendleft(vertex)
        graph.visited[vertex] = True
        while queue:
            v = queue.pop()
            print v
            queue.extendleft(
                adjv for adjv in graph.adjvertices[v]
                if not graph.visited[v]
            )
                           
def main():
    def genvertex(nv):
        for vertex in xrange(1, 16):
            yield chr(vertex + 96)

    bfsobj = BFS()
    graph = Graph(
        [

            Edge('b', 'a'), Edge('b', 'c'), Edge('b', 'd'), Edge('b', 'e'),
            Edge('b', 'f'), Edge('e', 'i'), Edge('e', 'j'), Edge('d', 'g'),
            Edge('d', 'h'), Edge('g', 'k'), Edge('g', 'l')
        ]
    )

    for v in genvertex(graph.nvertices):
        if not graph.visited[v]:
            bfsobj.search(graph, v)

if __name__ == '__main__':
    main()