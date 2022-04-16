import json
import os
import string
from Graph.edge import Edge
from Graph.utils.json_functions import get_data_from_json_file
from Graph.vertex import Vertex
import networkx as nx
from matplotlib import pyplot as plt

def get_project_name(path: string) ->string:
    projectName = os.path.basename(path)
    projectName = projectName[0:projectName.rindex('.')]
    return projectName

class Graph:
    def __init__(self, path :string = None, name :string='graph'):
        self.vertices :dict = {}            # key:vertex
        self.edges_dict :dict = {}               # key,key:edge
        self.edges :list = []
        self.name = name
        if(path):
            self.__build_graph_from_json(path)
            self.name: string = get_project_name(path)


##################################################################################3
    def num_of_vertices(self):
        return len(self.vertices)
    def num_of_edges(self):
        return len(self.edges_dict)
##################################################################################3
    def add_vertex(self, vertex: Vertex) -> None:
        self.vertices[vertex.key] = vertex
        self.edges_dict[vertex.key] = []
    def add_edge(self, edge: Edge):
        self.edges_dict[edge.source].append(edge)
        self.edges.append(edge)
##################################################################################3
    def get_vertices(self) ->list:
        return list(self.vertices.values())
    def get_edges(self) ->list:
        return list(self.edges)
    def get_vertex(self, key :int):
        return self.vertices[key]
    def get_edge(self,source_key :int, dest_key :int):
        return self.edges_dict[source_key, dest_key]
##################################################################################3
    def draw(self) ->None:
        G = nx.DiGraph()
        edges = []
        edge_labels = dict()
        for edges_list in self.edges_dict.values():
            for edge in edges_list:
                v1 :string = self.get_vertex(edge.source).name
                v2 :string = self.get_vertex(edge.to).name
                edges.append((v1,v2))
                edge_labels[v1,v2] = edge.type
        G.add_edges_from(edges)

        pos = nx.spring_layout(G, k=500)
        nx.draw_networkx_nodes(G, pos, cmap=plt.get_cmap('jet'),node_size=2000,node_color='#00b4d9')
        nx.draw_networkx_labels(G, pos, font_size=10, font_color='k')
        nx.draw_networkx_edges(G, pos, edge_color = 'b')
        nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)
        plt.show()
##################################################################################3
    def __len__(self):
        return len(self.vertices)
    def __str__(self):
        s = ''
        for vertex in self.get_vertices():
            s += str(vertex) + ' '
        for edge in self.get_edges():
            s += str(edge) + ' '
        return s
##################################################################################3
    def __build_graph_from_json(self, path :string):
        data :json = get_data_from_json_file(path)
        self.__add_vertices_from_json(data['vertices'])
        self.__add_edges_from_json(data['edges'])
    def __add_vertices_from_json(self, vertices :json):
        for v in vertices:
            key = v['key']
            name = v['name']
            type = v['type']
            try:
                attributes = v['attributes']
                vertex = Vertex(key, name, type, attributes)
            except:
                vertex = Vertex(key, name, type)
            self.add_vertex(vertex)
    def __add_edges_from_json(self, edges :json):
        for e in edges:
            type = e['type']
            source = e['from']
            to = e['to']
            edge = Edge(source, to, type)
            self.add_edge(edge)
##################################################################################3
    def bfs(self, source: int, goal: int) -> list:
        visited = set()
        queue = [source]
        edges = {source:[]}
        while (len(queue) > 0):
            size = len(queue)
            while (size > 0):
                curr = queue.pop()
                visited.add(curr)
                if (curr == goal):
                    res = []
                    for list in edges.values():
                        for edge in list:
                            res.append(edge)
                    return res
                else:
                    for edge in self.edges_dict[curr]:
                        if not visited.__contains__(edge.to):
                            queue.append(edge.to)
                            edges[curr].append(edge)
                            edges[edge.to] = []
                size-=1
        return None


if __name__ == '__main__':
    path = '../Files/graphs/src1.json'
    x = get_data_from_json_file('../Files/graphs/src1.json')
    g = Graph(path)
    print(len(g))
    print(g.num_of_vertices(),'vertices',g.num_of_edges(),'edges')
    for v in g.get_vertices():
        print(v)
    for e in g.get_edges():
        print(e)

