from ListGraph import Graph as LG
from MatrixGraph import Graph as MG

if __name__ == "__main__":

    listgrp = LG()
    matrxgrp = MG(6)

    listgrp.add_edge("A", "B", 4, True)
    listgrp.add_edge("A", "C", 2, True)
    listgrp.add_edge("B", "D", 5, True)
    listgrp.add_edge("C", "D", 8, True)
    listgrp.add_edge("C", "E", 3, True)
    listgrp.add_edge("D", "F", 6, True)
    listgrp.add_edge("E", "F", 1, True)

    #A - B - C - D - E - F
    matrxgrp.add_edge(0, 1, 4, True)
    matrxgrp.add_edge(0, 2, 2, True)
    matrxgrp.add_edge(1, 3, 5, True)
    matrxgrp.add_edge(2, 3, 8, True)
    matrxgrp.add_edge(2, 4, 3, True)
    matrxgrp.add_edge(3, 5, 6, True)
    matrxgrp.add_edge(4, 5, 1, True)

    print(listgrp.list)
    print(matrxgrp.matrix)



