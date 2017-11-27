import graph, Dijkstra, BFS, EdmondsKarp, Bipartite

def graph_1():
    g = {'s':{'b':10,'d':10},'b':{'c':9},'c':{'e':6,'t':10},'d':{'b':2,'c':8,'e':4},'e':{'t':10},'t':dict()}
    G = graph.graph(g)
    return G

def graph_2():
	L = ['a','b','c','d','e']
	R = ['f','g','h','i']
	g = {'a':{'f':1},'b':{'f':1,'h':1},'c':{'g':1,'h':1,'i':1},'d':{'h':1},'e':{'h':1,'i':1},'f':dict(),'g':dict(),'h':dict(),'i':dict(),'t':dict()}
	G = graph.graph(g)
	return G,L,R

print(EdmondsKarp.EdmondsKarp(graph_1(),'s','t'))

G,L,R = graph_2()
print(Bipartite.Bipartite(G,L,R))