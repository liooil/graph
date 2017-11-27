import graph, Dijkstra, BFS

def graph_1():
    g = {'s':{'b':10,'d':10},'b':{'c':9},'c':{'e':6,'t':10},'d':{'b':2,'c':8,'e':4},'e':{'t':10},'t':dict()}
    G = graph.graph(g)
    return G

G = graph_1()
Dijkstra.Dijkstra(G,'s','t')
for i in BFS.BFS(G,'s'):
    print(i)
