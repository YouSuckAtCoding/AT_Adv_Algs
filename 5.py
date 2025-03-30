import heapq
from ListGraph import Graph

def bfs(grp):

    firstNode = list(grp.list.keys())[0]

    visited = {edge: False for edge in grp.list}
    visited[firstNode] = True

    prev = [firstNode]
    pq = [(firstNode)]

    while pq:

        curr_node = heapq.heappop(pq)

        visited[curr_node] = True

        for key, value in grp.list[curr_node]:
            if not visited[key]:
                prev.append(key)
                heapq.heappush(pq, key)
                visited[key] = True

    return prev


def dfs_recusrsion(visited, node, result):

    visited[node] = True
    result.append(node)

    for key, weight in grp.list[node]:
        if not visited[key]:
            dfs_recusrsion(visited, key, result)

def dfs(grp):

    visited = {edge: False for edge in grp.list}

    result = []

    for key in grp.list:
        if not visited[key]:
            dfs_recusrsion(visited, key, result)

    return result

if __name__ == "__main__":

    grp = Graph()

    grp.add_edge("CD", "A", 4)
    grp.add_edge("CD", "B", 2)
    grp.add_edge("A", "C", 5)
    grp.add_edge("A", "D", 10)
    grp.add_edge("B", "A", 3)
    grp.add_edge("B", "D", 8)
    grp.add_edge("C", "D", 2)
    grp.add_edge("C", "E", 4)
    grp.add_edge("D", "E", 6)
    grp.add_edge("D", "F", 5)
    grp.add_edge("E", "F", 3)

    print(bfs(grp))
    print(dfs(grp))