import string
from Graph.edge import Edge
from Graph.graph import Graph
from Graph.vertex import Vertex, VertexTypeEnum


class GraphFromQuery(Graph):
    def __init__(self):
        Graph.__init__(self)
        self.classes_names: dict = {}  # name:vertex
        self.methods_names: dict = {}  # name:vertex
        self.interfaces_names: dict = {}  # name:vertex
        self.key = -1

    def get_key(self)->int:
        self.key += 1
        return self.key

    def add_class(self, name: string) -> Vertex:
        vertex = self.classes_names.get(name)
        if vertex:
            return vertex
        else:
            key = self.get_key()
            vertex = Vertex(key, name, 'class')
            super().add_vertex(vertex)

            self.vertices[key] = vertex
            self.classes_names[name] = vertex
            return vertex

    def add_edge(self, type: string, source_key: int, dest_key: int):
        edge = Edge(source_key, dest_key, type)
        super().add_edge(edge)


    def add_method(self, name, arguments=[], modifiers=[], return_type='') -> Vertex:
        key = self.get_key()
        vertex = Vertex(key, name, VertexTypeEnum.METHOD, arguments, modifiers)
        self.vertices[key] = vertex
        self.methods_names[name] = vertex
        return vertex

    def add_interface(self, name: string) -> Vertex:
        vertex = self.interfaces_names.get(name)
        if vertex:
            return vertex
        else:
            key = self.get_key()
            vertex = Vertex(key, name, VertexTypeEnum.INTERFACE)
            self.vertices[key] = vertex
            self.interfaces_names[name] = vertex
            return vertex
