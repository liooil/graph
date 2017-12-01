import graph, fib_heap

def Dijkstra(G,s,t,INF=99999):
    dists = dict()
    prevs = dict()
    nodes = dict()
    S=fib_heap.FibonacciHeap()
    for v in G.g:
        if v==s:
            dists[v]=0
        else:
            dists[v]=INF
        prevs[v]=None
        node_v=fib_heap.FibonacciHeap.Node(dists[v],v)
        nodes[v]=node_v
        S.Insert(node_v)
    v = S.extract_min().value
    while True:
        for u in G.g[v]:
            tmp = dists[v]+G.g[v][u]
            if tmp<dists[u]:
                dists[u]=tmp
                S.decrease_key(nodes[u],tmp)
                prevs[u]=v
        v=S.extract_min().value
        if v==t:
            break
    path = []
    while True:
        path.append(t)
        t = prevs[t]
        if t==s:
            return path+[s]
