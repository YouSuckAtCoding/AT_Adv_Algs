from MatrixGraph import Graph

if __name__ == "__main__":

    grp = Graph(6)

    #A - B - C - D - E - F
    grp.add_edge(0, 1, 5, True)
    grp.add_edge(0, 2, 10, True)
    grp.add_edge(1, 2, 3,True)
    grp.add_edge(1, 3, 8,True)
    grp.add_edge(2, 3, 2,True)
    grp.add_edge(2, 4, 7,True)
    grp.add_edge(3, 4, 4,True)
    grp.add_edge(3, 5, 6,True)
    grp.add_edge(4, 5, 5,True)

    print(grp.floyd())

    print(grp.matrix[0][5])
