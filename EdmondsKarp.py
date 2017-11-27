import graph, BFS
def get_path(G,s,t):
    if s==t:
        return [s]
    return get_path(G,s,G.prevs[t])+[t]
def EdmondsKarp(G,s,t, INF=99999):
    maxflow = 0
    while BFS.BFS(G, s, t):
        v = t
        # determine capacity
        capacity = INF
        while G.prevs[v]!=None:
            u = G.prevs[v]
            if capacity>G.g[u][v]:
                capacity = G.g[u][v]
            v = u
        v = t
        while G.prevs[v]!=None:
            u = G.prevs[v]
            G.g[u][v] = G.g[u][v]-capacity
            if G.g[u][v] == 0:
                del(G.g[u][v])
            if u not in G.g[v]:
                G.g[v][u] = capacity
            else:
                G.g[v][u] += capacity
            v = u
        maxflow += capacity
        print('%d:'%capacity,'->'.join(get_path(G,s,t)))
    return maxflow