class Node:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        return self
class BinarySearchTree:
    def __init__(self):
        self.root = None
        return self
    
    def insert(self,value):
        new_node = Node(value)
        if self.root == None:
                self.root = new_node
        elif self.root.value > value:
            self.root.left = new_node
        elif self.root.value < value:
            self.root.right = new_node
        return self
    
    def search(self,value):
        if self.root == None:
            return False
        else:
            while True:
             if  self.root.value == value:
        
        elif self.root.value > value:
            return self.root.left.search(value)
        elif self.root.value < value:
            return self.root.right.search(value)
        return False
b1 = BinarySearchTree()
b1.insert(10)

print(b1)
