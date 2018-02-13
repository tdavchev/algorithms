def minimum_spanning_tree(self):
    vertex_count = 0
    weight = 0

    current = self.g[0]
    current.visited = True
    vertex_count += 1

    while vertex_count < len(self.g):
        smallest = None
        for i in range(len(self.e)):
            if self.e[i].vsisited == False and self.e[i].dest.visited == False:
                smallest = self.e[i]
                break