from BeamSearch.BeamSearch import BeamSearch
from Graph.graphFromJson import GraphFromJson
from Query.query import Query


def testBeamSearch():
    graph = GraphFromJson('./Files/graphs/src1.json')

    query = Query("list iterable node")
    searcher = BeamSearch(graph)
    result = searcher.search(query, 2)

    print(result)
    result.draw()


def main():
    testBeamSearch()


if __name__ == '__main__':
    main()
