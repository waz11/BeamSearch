import json
import string
from Graph.vertex import Vertex

class Edge():

    def __init__(self, source:int, to:int, type:string):
        self.type :string = type
        self.source :Vertex = source
        self.to :Vertex = to

    def __str__(self):
        return "({}-{}->{})".format(self.source,self.type, self.to)
