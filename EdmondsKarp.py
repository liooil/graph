import graph, BFS
def EdmondsKarp(G,s,t):
    # flow := 0   (Initialize flow to zero)
    flow = 0
    while True:
    # repeat
        '''(Run a bfs to find the shortest s-t path.
         We use 'pred' to store the edge taken to get to each vertex,
         so we can recover the path afterwards)'''
        # q := queue()
        q = []
        # q.push(s)
        q.append(s)
        # pred := array(graph.length)
        pred = []
        # while not empty(q)
        while len(q) != 0:
            # cur := q.poll()
            u = q.pop(0)
            # for Edge e in graph[cur]
            for v, e in graph[u].items():
                 if pred[v] = null and v != s and e['cap'] > e['flow']

                    pred[e.t] := e
                    q.push(e.t)

        if not (pred[t] = null)
            (We found an augmenting path.
             See how much flow we can send)
            df := ∞
            for (e := pred[t]; e ≠ null; e := pred[e.s])
                df := min(df, e.cap - e.flow)
            (And update edges by that amount)
            for (e := pred[t]; e ≠ null; e := pred[e.s])
                e.flow  := e.flow + df
                e.rev.flow := e.rev.flow - df
            flow := flow + df
        if pred[t] == None:
            break
    # until pred[t] = null  (i.e., until no augmenting path was found)
    return flow
