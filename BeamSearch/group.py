from Graph.vertex import Vertex

def getDelta(model, c:Vertex, v:Vertex) ->float:
    delta = model.euclid(c, v)
    return delta

class Group:
    def __init__(self, vertex_key :int):
        self.vertices = set()
        self.vertices.add(vertex_key)
        self.cost = 0

    def __len__(self):
        return len(self.vertices)

    def add_vertex_key(self, key :int) ->None:
        self.vertices.add(key)

    def set_cost(self, val :float) ->None:
        self.cost = val

    def __str__(self):
        s='[ '
        for v in self.vertices:
            s+=v.name+' '+str(v.key)+','
        s+=']'
        return s