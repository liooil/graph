class graph:
    def __init__(self,g=dict()):
        self.g = g
        self.value = dict()
        for node in g:
            self.value[node] = 0
    def AddEdge(self,u,v,weight):
        self.g[u][v] = weight
    def RemoveEdge(self,u,v):
        del(self.g[u][v])
    def AddVertex(self,node,value=0):
        self.g[node] = dict()
        self.value[node] = value
    def RemoveVertex(self,node):
        for u in self.g:
            if node in self.g[u]:
                del(self.g[u][v])
        del(self.g[node])
        del(self.value[node])
    def IsAdjacent(self,u,v):
        return v in self.g[u]
    def GetEdgeWeight(self,u,v):
        return self.g[u][v]
    def SetEdgeWeight(self,u,v,weight):
        self.g[u][v] = weight
    def GetVertexValue(self,node):
        return self.value[node]
    def SetVertexValue(self,node_name,value):
        self.value[node] = value
    def printGraph(self):
        for u in self.g:
            print(u+':')
            if self.g[u]==dict():
                print("\tEmpty")
            for v in self.g[u]:
                print('\t',u,'->',v,':',self.g[u][v])
