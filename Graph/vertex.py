import json

from Parser.tokenizer import Tokenizer


class Vertex:

    def __init__(self,key:int, name, type, attributes=None):
        self.key = key
        self.type = type
        self.name = name

        self.neighbors = set()
        self.attributes = set()
        if attributes:
            for att in attributes: self.attributes.add(att)

        self.tokens = Tokenizer().get_tokens(name)

    def __str__(self):
        neighbors = []
        if self.neighbors:
            for neighbor in self.neighbors:
                neighbors.append(neighbor.name)
        return "[{},{},{}]".format(self.key, self.type, self.name)
