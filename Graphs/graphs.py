class Graph(object):
    def __init__(self, graph_dict=None):
        if graph_dict == None:
            graph_dict = {}

        self.__graph_dict = graph_dict

    def vertices(self):
        return list(self.__graph_dict.keys())

    def edges(self):
        return self.__generate_edges()

    def add_vertex(self, vertex):
        if vertex not in self.__graph_dict:
            self.__graph_dict[vertex] = []

    def add_edge(self, edges):
        edge = set(edges)
        (vertex1, vertex2) = tuple(edge)
        if vertex1 in self.__graph_dict:
            self.__graph_dict[vertex1].append(vertex2)
        else:
            self.__graph_dict[vertex1] = vertex2

    def __generate_edges(self):
        edges = []
        for node in self.__graph_dict:
            for neighbour in self.__graph_dict[node]:
                if (neighbour, node) not in edges:
                    edges.append((node, neighbour))

        return edges

    def __str__(self):
        res = "vertices: "
        for k in self.__graph_dict:
            res += str(k) + " "
        res += "\nedges:"
        for edge in self.__generate_edges():
            res += str(edge) + " "

        return res

    def find_all_paths2(self, start, end, path=[]):
        if start not in self.__graph_dict:
            return []

        path = path + [start]
        if start == end:
            return [path]

        all_paths = []
        
        for neighbour in self.__graph_dict[start]:
            if neighbour not in path:
                extended_path = self.find_all_paths2(neighbour, end, path)
                for p in extended_path:
                    all_paths.append(p)

        return all_paths

    def find_path2(self, start, end, path=None):
        if path is None:
            path = []

        path = path + [start]

        if start not in self.__graph_dict:
            return None

        if start == end:
            return path

        for neighbour in self.__graph_dict[start]:
            ans = None
            if neighbour not in path:
                ans = self.find_path2(neighbour, end, path)

            if ans:
                return ans

        return None

    def bfs(self, graph, start):
        visited, queue = set(), [start]
        while queue:
            vertex = queue.pop(0)
            if vertex not in visisted:
                visisted.add(vertex)
                queue.extend(self.__graph_dict[vertex] - visisted)

        return visisted

    def bfs_path(self, start, goal):
        queue = [(start, [start])]
        while queue:
            (vertex, path) = queue.pop(0)
            for next_ in (self.__graph_dict[vertex]):
                if next_ not in path:
                    if next_ == goal:
                        return path + [next_]
                    else:
                        queue.append((next_, path + [next_]))

        return None

    def breadth_first(self, start):
        level = {start:[]}
        parent = {start:None}
        i = 1
        frontier = {start}
        while frontier:
            next_ = []
            for vertex in frontier:
                for neighbour in self.__graph_dict[vertex]:
                    if neighbour not in level:
                        level[neighbour] = i
                        parent[neighbour] = vertex
                        next_.append(neighbour)

            frontier = next_
            i += 1

        return level, parent


    def find_path(self, start_node, end_node, path=[]):
        path = path + [start_node]
        if start_node not in self.__graph_dict:
            return None

        if start_node == end_node:
            return path

        for node in self.__graph_dict[start_node]:
            result = None
            if node not in path:
                result = self.find_path(node, end_node, path)

            if result:
                return result

        return None

    def find_all_paths(self, start_vertex, end_vertex, path=[]):
        graph = self.__graph_dict
        path = path + [start_vertex]
        if start_vertex == end_vertex:
            return [path]

        if start_vertex not in graph:
            return []

        paths = []
        for vertex in graph[start_vertex]:
            if vertex not in path:
                extended_paths = self.find_all_paths(vertex, end_vertex, path)
                for p in extended_paths:
                    paths.append(p)

        return paths

    def find_isolated_vertices(self):
        isolated = []
        for vertex in self.__graph_dict:
            if len(self.__graph_dict[vertex]) == 0:
                isolated.append(vertex)

        return isolated

    def vertex_degree(self, vertex):
        adj_vertices = self.__graph_dict[vertex]
        degree = len(adj_vertices) + adj_vertices.count(vertex)

        return degree

    def delta(self):
        min = 100000000000
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree < min:
                min = vertex_degree

        return min

    def Delta(self):
        max = 0
        for vertex in self.__graph_dict:
            vertex_degree = self.vertex_degree(vertex)
            if vertex_degree > max:
                max = vertex_degree

        return max

    def degree_sequence(self):
        seq = []
        for vertex in self.__graph_dict:
            seq.append(self.vertex_degree(vertex))

        seq.sort(reverse=True)
        return tuple(seq)

    def is_connected(self, vertices_encountered=None, start_vertex=None):
        if vertices_encountered is None:
            vertices_encountered = set()

        gdict = self.__graph_dict
        vertices = list(gdict.keys())
        if not start_vertex:
            start_vertex = vertices[0]

        vertices_encountered.add(start_vertex)
        if len(vertices_encountered) != len(vertices):
            for vertex in gdict[start_vertex]:
                if vertex not in vertices_encountered:
                    if self.is_connected(vertices_encountered, vertex):
                        return True
        else:
            return True

        return False

    def diameter(self):
        v = self.vertices()
        pairs = [(v[i], v[j]) for i in range(len(v)-1) for j in range(i+1, len(v))]
        smallest_path = []
        for (s,e) in pairs:
            paths = self.find_all_paths(s,e)
            smallest = sorted(paths, key=len)[0]
            smallest_path.append(smallest)

        smallest_path.sort(key=len)
        diameter = len(smallest_path[-1]) - 1
        return diameter

if __name__ == "__main__":
    g = {"a": ["d", "f"],
        "b": ["c"],
        "c": ["b", "c", "d", "e"],
        "d": ["a", "c"],
        "e": ["c"],
        "f": ["d"]}

    graph = Graph(g)
    # path = graph.find_path("a", "b")

    path = graph.find_path("a", "b")
    # print(path)

    path = graph.find_path2("a", "b")
    print(path)

    path = graph.bfs_path("a", "b")
    print(path)

    # deg = graph.vertex_degree("a")
    # print(deg)