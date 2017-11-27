import graph, fib_heap

def Dijkstra(G,s,t,INF=99999):
    nodes = dict()
    S=fib_heap.FibonacciHeap()
    for v in G.g:
        if v==s:
            G.dists[v]=0
        else:
            G.dists[v]=INF
        G.prevs[v]=None
        node_v=fib_heap.FibonacciHeap.Node(G.dists[v],v)
        nodes[v]=node_v
        S.Insert(node_v)
    v = S.extract_min().value
    while True:
        for u in G.g[v]:
            tmp = G.dists[v]+G.g[v][u]
            if tmp<G.dists[u]:
                G.dists[u]=tmp
                S.decrease_key(nodes[u],tmp)
                G.prevs[u]=v
        v=S.extract_min().value
        if v==t:
            break
    path = []
    while True:
        path.append(t)
        t = G.prevs[t]
        if t==s:
            return path+[s]
