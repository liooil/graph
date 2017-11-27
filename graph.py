class graph:
    def __init__(self,g=dict()):
        self.g = g
        self.dists = dict()
        self.prevs = dict()
        for node in g:
            self.dists[node] = 0
            self.prevs[node] = None
    def AddEdge(self,u,v,weight):
        self.g[u][v] = weight
    def RemoveEdge(self,u,v):
        del(self.g[u][v])
    def AddVertex(self,node,dists=0):
        self.g[node] = dict()
        self.dists[node] = dists
    def RemoveVertex(self,node):
        for u in self.g:
            if node in self.g[u]:
                del(self.g[u][v])
        del(self.g[node])
        del(self.dists[node])
    def IsAdjacent(self,u,v):
        return v in self.g[u]
    def GetEdgeWeight(self,u,v):
        return self.g[u][v]
    def SetEdgeWeight(self,u,v,weight):
        self.g[u][v] = weight
    def GetVertexdists(self,node):
        return self.dists[node]
    def SetVertexdists(self,node_name,dists):
        self.dists[node] = dists
