class MinHeap:
    def __init__(self, A: list):
        self.heap = A
        self.heapify()

    def heapify_help_1(self, heap, size, i):
        smallest = i
        left_node = 2 * i + 1
        right_node = 2 * i + 2
        if left_node < size and heap[left_node] < heap[smallest]:
            smallest = left_node
        if right_node < size and heap[right_node] < heap[smallest]:
            smallest = right_node
        if smallest != i:
            heap[i], heap[smallest] = heap[smallest], heap[i]
            self.heapify_help_1(heap, size, smallest)

    def heapify(self):

        startIdx = len(self.heap) // 2 - 1
        for i in range(startIdx, -1, -1):
            self.heapify_help_1(self.heap, len(self.heap), i)

    def push(self, key):
        self.heap.append(key)
        self.heapify()

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        poped = self.heap.pop(-1)
        self.heapify()
        return poped

    def print(self):
        for i in range(len(self.heap)):
            print(self.heap[i], end=" ")
        print()


if __name__ == "__main__":
    heap = MinHeap([4, 8, 6, 5, 1, 2, 3])
    heap.print()        # 1 4 2 5 8 6 3
    print(heap.pop())   # 1
    heap.push(9)
    heap.print()        # 2 4 3 5 8 6 9
