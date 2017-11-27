import graph
def BellmanFord(G,s,t,INF=99999):
    for v in G.g:
        if v!=s:
            G.dists[v] = INF
            G.prevs[v] = None
        else:
            G.dists[v] = 0
    for count in range(1,len(G.g)):
        for u in G.g:
            for v in G.g[u]:
                tmp = G.dists[u] + G.g[u][v]
                if tmp<G.dists[v]:
                    G.dists[v] = tmp
                    G.prevs[v] = u
    path = []
    while True:
        path.append(t)
        t = G.prevs[t]
        if t==s:
            return path+[s]
