import random

from MatrixGraph import Graph

if __name__ == "__main__":

    grp = Graph(6)

    grp.add_edge(0, 1, 5)
    grp.add_edge(0, 2, 10)
    grp.add_edge(1, 2, 3)
    grp.add_edge(1, 3, 8)
    grp.add_edge(2, 3, 2)
    grp.add_edge(2, 4, 7)
    grp.add_edge(3, 4, 4)
    grp.add_edge(3, 5, 6)
    grp.add_edge(4, 5, 5)

    grp.primMst()


    grp = Graph(26)

    for i in range(26):
        for j in range(i + 1, 26):
            weight = random.randint(1, 100)
            grp.add_edge(i, j, weight)

    grp.primMst()
