import random
import time

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


    start_time = time.time()
    grp.primMst()
    print("Tempo para grafo pequeno: ", time.time() - start_time)

    grp = Graph(150)

    for i in range(150):
        for j in range(i + 1, 150):
            weight = random.randint(1, 100)
            grp.add_edge(i, j, weight)

    start_time = time.time()
    grp.primMst()
    print("Tempo para grafo grande: ", time.time() - start_time)
