class Node:
    def __init__(self):
        self.body = None
        self.next = None

class linkL:
    def __init__(self):
        self.head = None

    def append(self,item):
        if self.head is None:
            self.head = Node()
            self.head.body = item
        else:
            head = self.head
            prev = None
            while head:
                prev = head
                head = head.next
            head = Node()
            head.body = item
            prev.next = head

    def pop(self):
        if self.head is None:
            return None

        if self.head.next is None:
            val = self.head.body
            self.head = None
            return val

        head = self.head
        prev = None

        while head.next:
            prev = head
            head = head.next

        prev.next = None
        return head.body
    
    def pop_front(self):
        if self.head is None:
            return None
        thing = self.head.body
        self.head = self.head.next
        return thing

    def insert(self, pos, item):
        if pos == 0:
            node = Node()
            node.body = item
            node.next = self.head
            self.head = node
            return

        head = self.head
        prev = None

        for i in range(pos):
            if head is None:
                return -1
            prev = head
            head = head.next

        node = Node()
        node.body = item
        node.next = head
        prev.next = node

    def peek(self):
        head = self.head
        if head is None:
            return None
        prev = None
        prev2 = None
        while head:
            prev2 = prev
            prev = head
            head = head.next
        return prev.body
    
    def print(self):
        head = self.head
        while head:
            print(head.body,end=",")
            head = head.next
        print()
    
    def __len__(self):
        count = 0
        head = self.head
        while head:
            count += 1
            head = head.next
        return count
    
    def __getitem__(self, index):
        head = self.head
        for i in range(index):
            if head is None:
                raise IndexError
            head = head.next
        if head is None:
            raise IndexError
        return head.body


class priorityQL:
    def __init__(self):
        self.body = linkL()

    def enqueue(self, item, priority):
        node = Node()
        node.body = [priority, item]

        body = self.body.head
        prev = None

        while body:
            if priority < body.body[0]:
                # insert at front
                if prev is None:
                    node.next = self.body.head
                    self.body.head = node
                else:
                    node.next = body
                    prev.next = node
                return

            prev = body
            body = body.next

        # insert at end
        if prev is None:
            self.body.head = node
        else:
            prev.next = node

    def dequeue(self):
        if len(self.body) == 0:
            return None
        return self.body.pop_front()


class priorityQH:
    def __init__(self):
        self.body = min_heap()

    def enqueue(self, item, priority):
        self.body.enqueue([priority, item])

    def dequeue(self):
        if len(self.body.body) == 0:
            return None
        return self.body.dequeue()

class min_heap:
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
            smallest = i
            left = 2*i + 1
            right = 2*i + 2

            if left < n and self.body[left][0] < self.body[smallest][0]:
                smallest = left

            if right < n and self.body[right][0] < self.body[smallest][0]:
                smallest = right

            if smallest == i:
                break

            self.body[i], self.body[smallest] = self.body[smallest], self.body[i]
            i = smallest

    # helper: move node up
    def _sift_up(self, i):
        while i > 0:
            parent = (i - 1) // 2

            if self.body[parent][0] <= self.body[i][0]:
                break

            self.body[parent], self.body[i] = self.body[i], self.body[parent]
            i = parent

    # add element
    def enqueue(self, value):
        self.body.append(value)
        self._sift_up(len(self.body)-1)

    # remove min element
    def dequeue(self):
        if len(self.body) == 0:
            return None

        root = self.body[0]
        last = self.body.pop()

        if len(self.body) > 0:
            self.body[0] = last
            self._sift_down(0)

        return root
    

import random
import timeit

# Step 1: generate random task list
def generate_tasks(n=1000):
    tasks = []
    for _ in range(n):
        if random.random() < 0.7:
            # enqueue
            value = random.randint(1, 1000)
            priority = random.randint(1, 100)
            tasks.append(("enqueue", value, priority))
        else:
            # dequeue
            tasks.append(("dequeue",))
    return tasks


# Step 2: runner for linked list PQ
def run_priorityQL(tasks):
    pq = priorityQL()
    for task in tasks:
        if task[0] == "enqueue":
            _, val, pr = task
            pq.enqueue(val, pr)
        else:
            pq.dequeue()


# Step 2: runner for heap PQ
def run_priorityQH(tasks):
    pq = priorityQH()
    for task in tasks:
        if task[0] == "enqueue":
            _, val, pr = task
            pq.enqueue(val, pr)
        else:
            pq.dequeue()


# Generate tasks once (important for fair comparison)
tasks = generate_tasks(1000)

# Measure time
time_ql = timeit.timeit(lambda: run_priorityQL(tasks), number=1)
time_qh = timeit.timeit(lambda: run_priorityQH(tasks), number=1)

# Results
print("Linked List PQ total time:", time_ql)
print("Heap PQ total time:", time_qh)

print("Linked List PQ avg per task:", time_ql / len(tasks))
print("Heap PQ avg per task:", time_qh / len(tasks))


# 4. Discussion:
# The heap-based priority queue (priorityQH) is faster than the linked list
# implementation (priorityQL). This is because the heap performs both enqueue
# and dequeue operations in O(log n) time, while the linked list requires O(n)
# time for enqueue since it must traverse the list to find the correct position.
# Although dequeue in the linked list is O(1), the frequent O(n) insertions make
# it slower overall. Therefore, the heap is more efficient for large numbers of tasks.