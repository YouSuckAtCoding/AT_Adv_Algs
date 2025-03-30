from ListGraph import Graph

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

    for x in grp.list:
        print(x, grp.list.get(x))


    print(grp.djikstra("CD", "F"))

    