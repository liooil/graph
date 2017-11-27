import graph
def BFT(G, s, INF=99999):
    for v in G.g:
        G.dists[v] = INF
        G.prevs[v] = None
    Q = []
    G.dists[s] = 0
    Q.append(s)
    while len(Q)!=0:
        v = Q.pop(0)
        for u in G.g[v]:
            if G.dists[u]==INF:
                G.dists[u] = G.dists[v]+1
                G.prevs[u] = v
                Q.append(u)
                yield u
def BFS(G, s, t):
    for u in BFT(G, s):
        if u==t:
            return True
    return False