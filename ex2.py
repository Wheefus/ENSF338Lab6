# Exercise #2

import random
import timeit

class Node:
    left = None
    right = None

    def __init__(self, data, parent=None):
        self.data = data
        self.parent = parent
        
def tree_insert(data, root=None):
    current = root
    parent = None

    while current is not None:
        parent = current
        if data <= current.data:
            current = current.left
        else:
            current = current.right

    if root is None:
        root = Node(data)
    elif data <= parent.data:
        parent.left = Node(data, parent)
    else:
        parent.right = Node(data, parent)

def tree_search(data, root):
    current = root
    while current is not None:
        if data == current.data:
            return current
        elif data < current.data:
            current = current.left
        else:
            current = current.right
    return None

def arr_search(data, arr, first, last):
    if first <= last:
        mid = (first + last)//2
        if data == arr[mid]:
            return mid
        elif data < arr[mid]:
            return arr_search(data, arr, first, mid-1)
        elif data > arr[mid]:
            return arr_search(data, arr, mid+1, last)
    return -1



def main():
    arr = [x for x in range(10000)]
    random.shuffle(arr)
    tree_head = Node(arr[0])

    for i in range(1,10000):
        tree_insert(arr[i], tree_head)

    total_time = 0
    for i in arr:
        total_time += timeit.timeit(lambda: tree_search(arr[i], tree_head), number=10)/10
    
    avg = total_time/10000
    print("Binary Tree")
    print(f"Total time taken: {total_time}")
    print(f"Average time taken: {avg}\n")

    arr.sort()
    total_time = 0
    for i in arr:
        total_time += timeit.timeit(lambda: arr_search(arr[i], arr, 0, 9999), number=10)/10
    
    avg = total_time/10000
    print("Array")
    print(f"Total time taken: {total_time}")
    print(f"Average time taken: {avg}\n")


main()

# 4. Discuss: which approach is faster? Why do you think is that? [0.2 pts]

# Binary tree is faster.
# I would think that this is due to not needing to do index arithmetic to find mid
