import timeit
import random
class Node:
    def __init__(self,data,parent = None):
        self.left = None
        self.data = data
        self.right = None
        self.parent = parent

class Binary_Search_Tree:
    def __init__(self):
        self.root = None
    
    def insert(self, data):

        current = self.root

        parent = None

        while current is not None:

            parent = current

            if data <= current.data:

                current = current.left

            else:

                current = current.right

        if self.root is None:

            self.root = Node(data)

        elif data <= parent.data:

            parent.left = Node(data, parent)

        else:

            parent.right = Node(data, parent)

    def search(self, data):

        current = self.root

        while current is not None:

            if data == current.data:

                return current

            elif data < current.data:

                current = current.left

            else:

                current = current.right

        return None
    

def add_list(l):
    out = 0
    for i in l:
        out += i
    return out

tree = Binary_Search_Tree()
values = list(range(10000))
for i in values:
    tree.insert(i)


total = 0
for i in values:
    total += timeit.timeit(lambda: tree.search(i), number=10)/10
avg = total/10000
print(f"total time  for 1: {total}")
print(f"sum of average times for 1: {add_list(avg)}")

random.shuffle(values)
tree2 = Binary_Search_Tree()
for i in values:
    tree2.insert(i)

total2 = 0
for i in values:
    total2 = timeit.timeit(lambda: tree2.search(i), number=10)/10

avg2 = total2/10000 
print(f"total time for 2: {total2}")
print(f"sum of average times for 2: {add_list(avg2)}")


# method 2 is faster because the tree is more balanced, in method 1 every value is inserted to
# the right so it takes O(n) to find an element while in method 2 the elements are randomly
# inserted allowing some to go to the left making it closer to O(log (n))
