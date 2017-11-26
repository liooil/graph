import fib_heap
class graph:
    def __init__(self,n):
        self.g = dict()
    def AddEdge(self,u,v,weight):
        self.g[u][v] = weight
    def RemoveEdge(self,u,v):
        del(self.g[u][v])
    def AddVertex(self,node):
        self.g[node] = dict()
    def RemoveVertex(self,node):
        for u in self.g:
            if node in self.g[u]:
                del(self.g[u][v])
        del(self.g[node])
    def IsAdjacent(self,u,v):
        return v in self.g[u]
    def GetEdgeWeight(self,u,v):
        return self.g[u][v]
    def SetEdgeWeight(self,u,v,weight):
        self.g[u][v] = weight
    def GetVertexValue(self,node):
        return self.g[node]['value']
    def SetVertexValue(self,node_name,value):
        self.g[node]['value'] = value
    def BellmanFord(self,s,t,INF=99999):
        dists = dict()
        prevs = dict()
        for v in self.g:
            if v!=s:
                dists[v] = INF
                prevs[v] = None
            else:
                dists[v] = 0
        for count in range(1,len(self.g)):
            for u in self.g:
                for v in self.g[u]:
                    tmp = dists[u] + self.g[u][v]
                    if tmp<dists[v]:
                        dists[v] = tmp
                        prevs[v] = u
        path = []
        while True:
            path.append(t)
            t = prevs[t]
            if t==s:
                return path+[s]
    def Dijkstra(self,s,t,INF=99999):
        dists = dict()
        prevs = dict()
        nodes = dict()
        S=fib_heap.FibonacciHeap()
        for v in self.g:
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
            for u in self.g[v]:
                tmp = dists[v]+self.g[v][u]
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
    def printGraph(self):
        for u in self.g:
            print(u+':')
            if self.g[u]==dict():
                print("\tEmpty")
            for v in self.g[u]:
                print('\t',u,'->',v,':',self.g[u][v])
