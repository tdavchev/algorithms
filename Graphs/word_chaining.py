class Graph(object):
    def __init__(self, graph=None):
        if graph is None:
            graph = {}

        self.graph = graph

    def add(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def __generate_edges(self):
        edges = []
        for node in self.graph:
            for neighbour in self.graph[node]:
                if (neighbour, node) not in edges:
                    edges.append((node, neighbour))

        return edges

    def add_edge(self, from_, _to):
        if _to not in self.graph[from_]:
            self.graph[from_] = _to

    def create_graph(self, bag_of_words):
        for i in range(len(bag_of_words)):
            self.add(str(bag_of_words[i][0]))

        for i in range(len(bag_of_words)):
            if str(bag_of_words[i][-1]) in self.graph:
                self.add_edge(str(bag_of_words[i][0]), str(bag_of_words[i][-1]))

    def find_cycle(self):
        edges = self.__generate_edges()
        path = []
        for out_, in_ in edges:
            path = path + [out_]
            if in_ in path:
                return True

        return False

    def __str__(self):
        res = "vertices: "
        res += str([key for key in self.graph.keys()])
        res += "\nedges: "
        res += str([val for val in self.__generate_edges()])

        return res

if __name__ == "__main__":
    graph = Graph()

    graph.create_graph(["eve", "eat", "ripe", "tear"])

    print(graph.find_cycle())