import graph
def BFS(G, s, INF=99999):
    dists = dict()
    prevs = dict()
    for v in G.g:
        dists[v] = INF
        prevs[v] = None
    Q = []
    dists[s] = 0
    Q.append(s)
    while len(Q)!=0:
        v = Q.pop(0)
        for u in G.g[v]:
            if dists[u]==INF:
                dists[u] = dists[v]+1
                prevs[u] = v
                Q.append(u)
                yield u
