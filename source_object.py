from constants import Constants
from node import Node


class SourceObject:
    def __init__(self, data):
        self.name = data.get(Constants.Keys.Source.name)
        self.sources = []

        for folder in data.get(Constants.Keys.Source.sources, []):
            node = Node(folder, '')
            self.sources.append(node)

    def __repr__(self):
        return '{} name: {}, sources: {}'.format(self.__class__, self.name, self.sources)
