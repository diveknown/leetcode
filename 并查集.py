class UnionFind:
    def __init__(self):
        self.father = {}
        self.num_of_sets = 0
    
    def find(self,x):
        root = x
        while self.father[root] != None:
            root = self.father[root]
        return root
    
    def merge(self,x,y):
        root_x = self.find(x)
        root_y = self.find(y)        
        if root_x != root_y:
            self.father[root_x] = root_y
            self.num_of_sets -= 1
    
    def add(self,x):
        if x not in self.father:
            self.father[x] = None
            self.num_of_sets += 1
