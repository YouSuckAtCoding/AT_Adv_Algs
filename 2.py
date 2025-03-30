import time
from MinHeap import MinHeap

class Package:
    def __init__(self, id, priority):
        self.id = id
        self.exec_time = time.time()
        self.priority = priority

    def __str__(self):
        return f"{self.id} -- {self.priority} -- {self.exec_time}"


if __name__ == "__main__":

    heap = MinHeap()

    packages = [
    Package(1,0),
    Package(2, 1),
    Package(3, 4),
    Package(4, 2),
    Package(5, 5),
    Package(6, 7),
    Package(7, 3),
    Package(8, 5),
    Package(9, 8),
    Package(10, 13)
    ]

    for pack in packages:
        heap.insert(pack)

    heap.printHeap()
    print()

    print("Delivering :", heap.getMin())
    heap.deliver()

    heap.printHeap()
    print()

    print("Updated Package with Id 10")
    heap.set_priority(10, 3)

    heap.printHeap()
    print()