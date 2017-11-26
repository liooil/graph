import graph, BFS

def graph_1():
    g=graph.graph()

    g.AddVertex('s')
    g.AddVertex('b')
    g.AddVertex('c')
    g.AddVertex('d')
    g.AddVertex('e')
    g.AddVertex('t')

    g.AddEdge('s','b',10)
    g.AddEdge('s','d',10)

    g.AddEdge('b','c',9)

    g.AddEdge('c','e',6)
    g.AddEdge('c','t',10)

    g.AddEdge('d','b',2)
    g.AddEdge('d','c',8)
    g.AddEdge('d','e',4)

    g.AddEdge('e','t',10)

    return g

myGraph = graph_1()
BFS.BFS(myGraph,'s')
