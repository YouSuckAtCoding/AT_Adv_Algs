import heapq


class Graph:

    def __init__(self):
        self.list = {}

    def add_edge(self, i, j, w, bidirectional=False):
        if i not in self.list:
            self.list[i] = []
        self.list[i].append((j, w))

        if j not in self.list:
            self.list[j] = []
        if bidirectional: self.list[j].append((i, w))

    def djikstra(self, src, dest):

        dist = {edge: float('inf') for edge in self.list}
        prev = {edge: None for edge in self.list}

        dist[src] = 0
        pq = [(0, src)]

        while pq:

            curr_dist, curr_edge = heapq.heappop(pq)

            if curr_edge == dest:
                print("Peso / Tempo / Custo de deslocamento:", dist[dest])
                return self.getShortestPath(src, dest, prev)

            for edge, weight in self.list[curr_edge]:
                newDist = curr_dist + weight
                if newDist < dist[edge]:
                    dist[edge] = newDist
                    prev[edge] = curr_edge
                    heapq.heappush(pq, (newDist, edge))

        return []

    def getShortestPath(self, src, dest, prev):
        path = []
        current_edge = dest

        while current_edge is not None:
            path.append(current_edge)
            current_edge = prev[current_edge]
        path.reverse()
        return path if path[0] == src else []







