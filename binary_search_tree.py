class Node(object):
    def __init__(self, key, value, left=None, right=None):
        self.key = key
        self.value = value
        self.left = left
        self.right = right


class BinarySearchTree(object):
    """
    implement binary search tree with node objects
    implement search, insert, delete binary search tree operations
    implement iterative and recursive binary search tree traversals
    """
    def __init__(self, iterable=None):
        self.root = None
        if iterable:
            for item in iterable:
                self.insert(item)

    def insert(self, key, value, node=None):
        if self.root is None:
            root_node = Node(key, value)
            self.root = root_node
            ## TODO: Fix la silly current node use - when I could just use node
        if node is None:
            current_node = self.root
        else:
            current_node = node
        # Not supposed to add the same key twice so need to check for that?
        if key > current_node.key:
            if current_node.right is None:
                new_node = Node(key, value)
                current_node.right = new_node
            else:
                self.insert(self, key, value, current_node.right)
        else:
            if current_node.left is None:
                new_node = Node(key, value)
                current_node.right = new_node
            else:
                self.insert(self, key, value, current_node.left)



    def delete(self, data):
        pass

    def search_iterative(self, key):
        current_node = self.root
        while current_node is not None:
            if key == current_node.key:
                return current_node
            elif key > current_node.key:
                current_node = current_node.right
            else:
                current_node = current_node.left
        raise KeyError, 'Could not find the key'

    def search_recursive(self, data):
        pass


bst = BinarySearchTree()
bst.insert(3, 5)
print bst.search_iterative(3).value
print(bst)
