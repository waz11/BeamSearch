from BeamSearch.BeamSearch import BeamSearch
from Graph.graphFromJson import GraphFromJson
from Query.query import Query


def testBeamSearch():
    graph = GraphFromJson('./Files/graphs/src1.json')

    # query = Query("list iterable node")
    # searcher = BeamSearch(graph)
    # result = searcher.search(query, 2)
    #
    # print(result)
    # result.draw()

    # print(result.num_of_vertices())
    # print(result.num_of_edges())
    # searcher.model.db.print_table('src1')
    # searcher.model.db.delete_db()

def main():
    testBeamSearch()


if __name__ == '__main__':
    main()
