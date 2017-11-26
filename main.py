import graph, BFS

def graph_1():
    g=graph.graph();
    # g=NewDense(6);

    g.AddVertex('a');
    g.AddVertex('b');
    g.AddVertex('c');
    g.AddVertex('d');
    g.AddVertex('e');
    g.AddVertex('t');

    g.AddEdge('a','b',-4);
    g.AddEdge('a','t',-3);
    g.AddEdge('b','d',-1);
    g.AddEdge('b','e',-2);
    g.AddEdge('c','b',8);
    g.AddEdge('c','t',3);
    g.AddEdge('d','a',6);
    g.AddEdge('d','t',4);
    g.AddEdge('e','c',-3);
    g.AddEdge('e','t',2);

    return g

myGraph = graph_1()
BFS.BFS(myGraph,'a')
