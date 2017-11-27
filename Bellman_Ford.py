import graph
def BellmanFord(G,s,t,INF=99999):
    dists = dict()
    prevs = dict()
    for v in G.g:
        if v!=s:
            dists[v] = INF
            prevs[v] = None
        else:
            dists[v] = 0
    for count in range(1,len(G.g)):
        for u in G.g:
            for v in G.g[u]:
                tmp = dists[u] + G.g[u][v]
                if tmp<dists[v]:
                    dists[v] = tmp
                    prevs[v] = u
    path = []
    while True:
        path.append(t)
        t = prevs[t]
        if t==s:
            return path+[s]
