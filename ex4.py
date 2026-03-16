import random
class max_heap:
    def __init__(self):
        self.body = []

    # turn an input array into a heap
    def heapify(self, array):
        self.body = array[:]
        n = len(self.body)

        for i in range(n//2 - 1, -1, -1):
            self._sift_down(i)

        return self.body

    # helper: move node down
    def _sift_down(self, i):
        n = len(self.body)

        while True:
            largest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < n and self.body[left] > self.body[largest]:
                largest = left

            if right < n and self.body[right] > self.body[largest]:
                largest = right

            if largest == i:
                break

            self.body[i], self.body[largest] = self.body[largest], self.body[i]
            i = largest

    # helper: move node up
    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self.body[parent] >= self.body[i]:
                break

            self.body[parent], self.body[i] = self.body[i], self.body[parent]
            i = parent

    # add element
    def enqueue(self, value):
        self.body.append(value)
        self._sift_up(len(self.body)-1)

    # remove max element
    def dequeue(self):
        if len(self.body) == 0:
            return None

        root = self.body[0]
        last = self.body.pop()

        if len(self.body) > 0:
            self.body[0] = last
            self._sift_down(0)

        return root
    
heap = max_heap()

arr = [10,9,8,7,6,5,4]
result = heap.heapify(arr)

expected = [10,9,8,7,6,5,4]

print(f"Test 1: result:{result} and expected:{expected}")

heap = max_heap()

arr = []
result = heap.heapify(arr)

expected = []

print(f"Test 2: result:{result} and expected:{expected}")

heap = max_heap()

arr = list(range(100))
result = heap.heapify(arr)

expected = [99, 94, 98, 78, 93, 97, 62, 70, 77, 86, 92, 96, 54, 58, 61, 66, 69, 74, 76, 82, 85, 90, 91, 95, 50, 52, 53, 56, 57, 60, 30, 64, 65, 68, 34, 72, 73, 75, 38, 80, 81, 84, 42, 88, 89, 45, 46, 47, 48, 49, 11, 51, 25, 12, 26, 55, 27, 13, 28, 59, 29, 14, 6, 63, 31, 15, 32, 67, 33, 16, 7, 71, 35, 17, 36, 3, 37, 18, 8, 79, 39, 19, 40, 83, 41, 20, 9, 87, 43, 21, 44, 4, 1, 22, 10, 2, 0, 23, 5, 24] 

print(f"Test 3: result:{result} and expected:{expected}")