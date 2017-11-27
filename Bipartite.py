import graph, EdmondsKarp

def Bipartite(G, L, R):
	s = 's'
	t = 't'
	G.g[s] = dict()
	G.g[t] = dict()
	for u in L:
		G.g[s][u] = 1
	for u in R:
		G.g[u][t] = 1
	return EdmondsKarp.EdmondsKarp(G, s, t)