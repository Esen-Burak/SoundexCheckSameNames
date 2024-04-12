class Node:
    def __init__(self):
        self.values = []
        self.children = {}

def insert(root, code, name):
    current = root
    for char in code:
        if char not in current.children:
            current.children[char] = Node()
        current = current.children[char]
    current.values.append(name)

def find_values(root, code):
    current = root
    for char in code:
        if char in current.children:
            current = current.children[char]
        else:
            return []
    return current.values