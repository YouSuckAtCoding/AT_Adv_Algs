class MinHeap:
    def __init__(self):
        self.arr = []

    def getMin(self):
        if len(self.arr) > 0:
            return self.arr[0]
        return None

    def deliver(self):
        if len(self.arr) > 0:
            self.delete(self.arr[0].id)
        return

    def insert(self, val):
        self.arr.append(val)
        i = len(self.arr) - 1

        self.moveUpHeap(i)

    def delete(self, id):

        i = -1

        for j in range(len(self.arr)):
            if self.arr[j].id == id:
                i = j
                break
        if i == -1:
            return

        self.arr[i] = self.arr[-1]
        self.arr.pop()

        self.moveDownHeap(idx=i, size=len(self.arr))

    def moveUpHeap(self, idx):
        while idx > 0 and self.arr[(idx - 1) // 2].priority > self.arr[idx].priority:
            self.arr[idx], self.arr[(idx - 1) // 2] = self.arr[(idx - 1) // 2], self.arr[idx]
            idx = (idx - 1) // 2

    def moveDownHeap(self, idx, size):

        while True:

            left = 2 * idx + 1
            right = 2 * idx + 2
            smallest = idx
            if left < size and self.arr[left].priority < self.arr[smallest].priority:
                smallest = left
            if right < size and self.arr[right].priority < self.arr[smallest].priority:
                smallest = right
            if smallest != idx:
                self.arr[idx], self.arr[smallest] = self.arr[smallest], self.arr[idx]
                idx = smallest
            else:
                break

    def search(self, id):
        for j in self.arr:
            if j.id == id:
                return True
        return False

    def set_priority(self, id, priority):

        for j in range(len(self.arr)):

            if self.arr[j].id == id:

                curr_priority = self.arr[j].priority
                self.arr[j].priority = priority

                if curr_priority > priority:
                    self.moveUpHeap(j)
                else:
                    self.moveDownHeap(j, len(self.arr))

                return

        return False

    def printHeap(self):
        for p in range(len(self.arr)):
            print(self.arr[p])