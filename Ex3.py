class Node:
    def __init__(self, data):
        self.data = data
        self.left = None  # Reference to the left child, initially None
        self.right = None # Reference to the right child, initially None

# # Create the nodes
# root = Node('R')
# nodeA = Node('A')
# nodeB = Node('B')
# nodeC = Node('C')
# nodeD = Node('D')

# # Link the nodes to form the tree
# root.left = nodeA
# root.right = nodeB
# nodeA.left = nodeC
# nodeA.right = nodeD

# The resulting tree structure:
#       R
#      / \
#     A   B
#    / \
#   C   D

def requestInput():
    ## get input and call functions
    inputA = ""
    inputA = input("Enter Input Here : ")
    inputA = inputA.replace(' ', '')
    print(inputA)
    print(str2tree(inputA))
    root = str2tree(inputA)
    result = operate(root)
    print(result)


def str2tree(s: str) -> Node:
    ## parse the string given by requestInput
    def parse_expression(s, index):
        left, index = parse_term(s, index)
        while index < len(s) and s[index] in '+-':
            op = s[index]
            index += 1
            right, index = parse_term(s, index)
            node = Node(op)
            node.left = left
            node.right = right
            left = node
        return left, index
    
    def parse_term(s, index):
        left, index = parse_factor(s, index)
        while index < len(s) and s[index] in '*/':
            op = s[index]
            index += 1
            right, index = parse_factor(s, index)
            node = Node(op)
            node.left = left
            node.right = right
            left = node
        return left, index
    
    def parse_factor(s, index):
        if s[index] == '(':
            index += 1
            node, index = parse_expression(s, index)
            index += 1  # skip ')'
            return node, index
        else:
            j = index
            while j < len(s) and s[j].isdigit():
                j += 1
            return Node(int(s[index:j])), j
    
    root, _ = parse_expression(s, 0)
    return root



def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    return a / b

## go through the tree from root and do the operations

def operate(rootNode):
    if rootNode is None:
        return 0
    
    # If it's a leaf node (number), return its value
    if isinstance(rootNode.data, int):
        return rootNode.data
    
    # Recursively evaluate left and right subtrees
    left_value = operate(rootNode.left)
    right_value = operate(rootNode.right)
    
    # Apply the operation based on the node's data
    if rootNode.data == '+':
        return add(left_value, right_value)
    elif rootNode.data == '-':
        return subtract(left_value, right_value)
    elif rootNode.data == '*':
        return multiply(left_value, right_value)
    elif rootNode.data == '/':
        return divide(left_value, right_value)

requestInput()