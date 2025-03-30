class Graph:

    def __init__(self, v):
        self.vertices = v
        self.matrix = [[float('inf') for _ in range(v)] for _ in range(v)]

    def add_edge(self, i, j, weight, bidirectional=False):
        self.matrix[i][j] = weight
        if bidirectional: self.matrix[j][i] = weight

    def __printMST(self, parent):
        total = 0
        print("Edge \tWeight")
        for i in range(1, self.vertices):
            print(chr(65 + parent[i]), "-", chr(65 + i), "\t", self.matrix[parent[i]][i])
            total += self.matrix[parent[i]][i]
        return total

    def minDist(self, dist, visited):

        min = float('inf')

        for x in range(self.vertices):
            if dist[x] < min and visited[x] == False:
                min = dist[x]
                min_index = x

        return min_index

    def primMst(self):

        dist = [float('inf')] * self.vertices
        mst = [None] * self.vertices
        visited = [False] * self.vertices

        dist[0] = 0
        mst[0] = -1

        for x in range(self.vertices):

            u = self.minDist(dist, visited)

            visited[u] = True

            for j in range(self.vertices):
                if self.matrix[u][j] != float('inf') and visited[j] == False \
                        and dist[j] > self.matrix[u][j]:
                    dist[j] = self.matrix[u][j]
                    mst[j] = u

        return self.__printMST(mst)

    def floyd(self):

        resMatrx = self.matrix

        prev = [[None] * self.vertices for _ in range(self.vertices)]
        nodes = [i for i in range(0, self.vertices)]

        for i in range(self.vertices):
            for j in range(self.vertices):
                if i != j and self.matrix[i][j] != -1:
                    prev[i][j] = nodes[i]

        for k in range(self.vertices):
            for i in range(self.vertices):
                for j in range(self.vertices):
                    if resMatrx[i][j] > resMatrx[i][k] + resMatrx[k][j]:
                        resMatrx[i][j] = resMatrx[i][k] + resMatrx[k][j]
                        prev[i][j] = prev[k][j]

        return resMatrx

    def reconstruct_path(self, previous_node, start, end):
        nodes = [i for i in range(len(previous_node))]
        path = []
        current = end
        while current is not None and current != start:
            path.append(chr(65 + current))
            current = previous_node[nodes.index(start)][nodes.index(current)]
        if current is None:
            print(f"No path from {start} to {end}.")
            return
        path.append(chr(65 + start))
        path.reverse()
        return path
