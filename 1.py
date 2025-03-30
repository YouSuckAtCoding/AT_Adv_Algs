import time
from MinHeap import MinHeap

class Process:
    def __init__(self, id, priority ):
        self.id = id
        self.exec_time = time.time()
        self.priority = priority

    def __str__(self):
        return f"{self.id} -- {self.priority} -- {self.exec_time}"

if __name__ == "__main__":

    heap = MinHeap()

    processes = [
    Process(1,0),
    Process(2, 1),
    Process(3, 4),
    Process(4, 2),
    Process(5, 5),
    Process(6, 7),
    Process(7, 3)
    ]

    for process in processes:
        heap.insert(process)

    heap.printHeap()
    print()

    print(heap.getMin())
    print()

    heap.delete(1)


    print(heap.getMin())

    print()
    heap.printHeap()
    print()

    heap.set_priority(3, 0)


    heap.printHeap()
    print()

    heap.set_priority(2, 10)

    heap.printHeap()
    print()





